import httpx
import uuid
from typing import Optional
from app.config import get_settings
from app.services.resume_service import resume_service
from app.database import get_supabase

settings = get_settings()


class ChatService:
    """Service for handling AI chat with Ollama"""
    
    def __init__(self):
        self.api_url = settings.ollama_url
        self.model = settings.ollama_model
        self.supabase = get_supabase()
    
    async def get_ai_response(self, user_message: str, session_id: Optional[str] = None) -> tuple[str, str]:
        """
        Get AI response based on user message and resume context
        Returns: (response_text, session_id)
        """
        # Generate session ID if not provided
        if not session_id:
            session_id = str(uuid.uuid4())
        
        # Get resume context
        resume_context = await resume_service.get_full_resume_context()
        
        # Get chat history for this session
        chat_history = await self._get_chat_history(session_id)
        
        # Build messages for AI
        messages = [
            {
                "role": "system",
                "content": f"""You are an intelligent AI assistant representing Viharahamed M's portfolio. Your role is to help visitors learn about Viharahamed's background, skills, projects, and experience.

PERSONALITY & TONE:
- Be professional yet friendly and conversational
- Show enthusiasm about Viharahamed's work and achievements
- Be concise but informative
- Use a warm, welcoming tone

RESPONSE GUIDELINES:
1. Answer questions based ONLY on the resume information provided below
2. If asked about something not in the resume, politely say: "I don't have that specific information in my knowledge base, but feel free to reach out to Viharahamed directly via email or LinkedIn!"
3. For project questions, highlight the technical aspects and real-world impact
4. For skills questions, mention both technical proficiency and practical application
5. For contact requests, provide the email, phone, LinkedIn, and GitHub information
6. Keep responses focused and to-the-point (2-4 sentences for simple questions)
7. For complex questions, you can provide more detail but stay organized

RESUME INFORMATION:
{resume_context}

Remember: You're here to showcase Viharahamed's expertise and help visitors connect with him. Be helpful, accurate, and engaging!"""
            }
        ]
        
        # Add chat history
        messages.extend(chat_history)
        
        # Add current user message
        messages.append({
            "role": "user",
            "content": user_message
        })
        
        # Save user message to database
        await self._save_message(session_id, "user", user_message)
        
        try:
            # Call Ollama API
            async with httpx.AsyncClient(timeout=120.0) as client:
                response = await client.post(
                    f"{self.api_url}/api/chat",
                    headers={
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": self.model,
                        "messages": messages,
                        "stream": False,
                        "options": {
                            "temperature": 0.7,
                            "num_predict": 500
                        }
                    }
                )
                
                response.raise_for_status()
                data = response.json()
                
                ai_response = data["message"]["content"]
                
                # Save AI response to database
                await self._save_message(session_id, "assistant", ai_response)
                
                return ai_response, session_id
                
        except httpx.HTTPError as e:
            error_msg = f"HTTP Error calling Ollama: {str(e)}\nResponse text: {e.response.text if hasattr(e, 'response') and e.response else 'No response'}"
            print(error_msg)
            return "I'm sorry, I'm having trouble connecting to the AI service right now. Please make sure Ollama is running.", session_id
        except Exception as e:
            print(f"Error getting AI response: {e}")
            return "I'm sorry, something went wrong. Please try again.", session_id
    
    async def _get_chat_history(self, session_id: str, limit: int = 10) -> list:
        """Get recent chat history for context"""
        try:
            response = self.supabase.table('chat_history')\
                .select('role, content')\
                .eq('session_id', session_id)\
                .order('created_at', desc=False)\
                .limit(limit)\
                .execute()
            
            if response.data:
                return [{"role": msg["role"], "content": msg["content"]} for msg in response.data]
            return []
        except Exception as e:
            print(f"Error fetching chat history: {e}")
            return []
    
    async def _save_message(self, session_id: str, role: str, content: str):
        """Save message to chat history"""
        try:
            self.supabase.table('chat_history').insert({
                "session_id": session_id,
                "role": role,
                "content": content
            }).execute()
        except Exception as e:
            print(f"Error saving message: {e}")


# Singleton instance
chat_service = ChatService()
