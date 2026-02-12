import json
from typing import List, Dict, Any
from pathlib import Path


class ResumeService:
    """Service for fetching and formatting resume data from JSON knowledge base"""
    
    def __init__(self):
        # Load resume data from JSON file
        self.data_path = Path(__file__).parent.parent.parent / "data" / "resume_knowledge.json"
        self.resume_data = self._load_resume_data()
    
    def _load_resume_data(self) -> Dict[str, Any]:
        """Load resume data from JSON file"""
        try:
            if self.data_path.exists():
                with open(self.data_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                print(f"Warning: Resume knowledge file not found at {self.data_path}")
                return {}
        except Exception as e:
            print(f"Error loading resume data: {e}")
            return {}
    
    async def get_profile(self) -> Dict[str, Any]:
        """Get profile information"""
        personal = self.resume_data.get('personal_info', {})
        education = self.resume_data.get('education', {}).get('current', {})
        
        # Return in format expected by frontend
        return {
            'name': personal.get('name', ''),
            'title': 'Full Stack Developer',
            'bio': f"A passionate Full Stack Developer ,worked with frontend and built some applications using React.js and some other libraries and frameworks.",
            'email': personal.get('email', ''),
            'phone': personal.get('phone', ''),
            'location': personal.get('location', ''),
            'linkedin': personal.get('linkedin', ''),
            'github': personal.get('github', '')
        }
    
    async def get_experiences(self) -> List[Dict[str, Any]]:
        """Get work experiences"""
        internship = self.resume_data.get('internship', {})
        if internship:
            # Return in format expected by frontend
            return [{
                'company': internship.get('company', ''),
                'position': internship.get('role', ''),
                'location': internship.get('location', ''),
                'start_date': '2025-06-01',
                'end_date': '2025-06-30',
                'description': '\n'.join(internship.get('responsibilities', [])),
                'technologies': internship.get('technologies_used', [])
            }]
        return []
    
    async def get_projects(self) -> List[Dict[str, Any]]:
        """Get projects"""
        projects = self.resume_data.get('projects', [])
        # Convert to format expected by frontend
        return [{
            'title': proj.get('name', ''),
            'description': proj.get('description', ''),
            'technologies': proj.get('technologies', []),
            'github_url': '',
            'live_url': '',
            'image_url': proj.get('image_url', ''),
            'featured': True
        } for proj in projects]
    
    async def get_skills(self) -> List[Dict[str, Any]]:
        """Get skills"""
        technical_skills = self.resume_data.get('technical_skills', {})
        
        # Convert to format expected by frontend (list of skill objects)
        skills_list = []
        category_map = {
            'programming_languages': 'Programming Languages',
            'web_technologies': 'Web Technologies',
            'databases': 'Databases',
            'soft_skills': 'Soft Skills'
        }
        
        for key, skill_names in technical_skills.items():
            if isinstance(skill_names, list):
                category = category_map.get(key, key.replace('_', ' ').title())
                for skill_name in skill_names:
                    skills_list.append({
                        'name': skill_name,
                        'category': category,
                        'proficiency': 'Advanced' if key == 'programming_languages' else 'Intermediate'
                    })
        
        return skills_list
    
    async def get_full_resume_context(self) -> str:
        """Get complete resume as formatted text for AI context"""
        if not self.resume_data:
            return "No resume information available."
        
        context = "=== VIHARAHAMED M - PORTFOLIO INFORMATION ===\n\n"
        
        # Personal Information
        personal = self.resume_data.get('personal_info', {})
        if personal:
            context += "📋 PERSONAL INFORMATION:\n"
            context += f"Name: {personal.get('name', 'N/A')}\n"
            context += f"Email: {personal.get('email', 'N/A')}\n"
            context += f"Phone: {personal.get('phone', 'N/A')}\n"
            context += f"LinkedIn: {personal.get('linkedin', 'N/A')}\n"
            context += f"GitHub: {personal.get('github', 'N/A')}\n"
            context += f"Location: {personal.get('location', 'N/A')}\n\n"
        
        # Education
        education = self.resume_data.get('education', {})
        if education:
            context += "🎓 EDUCATION:\n"
            current = education.get('current', {})
            if current:
                context += f"Current: {current.get('degree', 'N/A')}\n"
                context += f"  Institution: {current.get('institution', 'N/A')}\n"
                context += f"  Location: {current.get('location', 'N/A')}\n"
                context += f"  CGPA: {current.get('cgpa', 'N/A')} (Up to {current.get('upto_semester', 'N/A')})\n"
                context += f"  Expected Graduation: {current.get('expected_graduation', 'N/A')}\n"
            
            hsc = education.get('hsc', {})
            if hsc:
                context += f"HSC ({hsc.get('year', 'N/A')}): {hsc.get('percentage', 'N/A')} - {hsc.get('institution', 'N/A')}\n"
            
            sslc = education.get('sslc', {})
            if sslc:
                context += f"SSLC ({sslc.get('year', 'N/A')}): {sslc.get('institution', 'N/A')}\n"
            context += "\n"
        
        # Projects
        projects = self.resume_data.get('projects', [])
        if projects:
            context += "💼 PROJECTS:\n"
            for i, proj in enumerate(projects, 1):
                context += f"{i}. {proj.get('name', 'N/A')} ({proj.get('type', 'N/A')})\n"
                context += f"   Description: {proj.get('description', 'N/A')}\n"
                
                technologies = proj.get('technologies', [])
                if technologies:
                    context += f"   Technologies: {', '.join(technologies)}\n"
                
                highlights = proj.get('highlights', [])
                if highlights:
                    context += "   Key Features:\n"
                    for highlight in highlights:
                        context += f"   - {highlight}\n"
                context += "\n"
        
        # Internship
        internship = self.resume_data.get('internship', {})
        if internship:
            context += "🏢 INTERNSHIP EXPERIENCE:\n"
            context += f"Company: {internship.get('company', 'N/A')}\n"
            context += f"Role: {internship.get('role', 'N/A')}\n"
            context += f"Location: {internship.get('location', 'N/A')}\n"
            context += f"Period: {internship.get('period', 'N/A')}\n"
            
            responsibilities = internship.get('responsibilities', [])
            if responsibilities:
                context += "Responsibilities:\n"
                for resp in responsibilities:
                    context += f"- {resp}\n"
            context += "\n"
        
        # Technical Skills
        skills = self.resume_data.get('technical_skills', {})
        if skills:
            context += "🛠️ TECHNICAL SKILLS:\n"
            for category, skill_list in skills.items():
                if isinstance(skill_list, list):
                    context += f"{category.replace('_', ' ').title()}: {', '.join(skill_list)}\n"
            context += "\n"
        
        # Certifications
        certifications = self.resume_data.get('certifications', [])
        if certifications:
            context += "📜 CERTIFICATIONS:\n"
            for cert in certifications:
                context += f"- {cert.get('name', 'N/A')} (Issuer: {cert.get('issuer', 'N/A')})\n"
            context += "\n"
        
        # Domain Expertise
        domains = self.resume_data.get('domain_expertise', [])
        if domains:
            context += "🎯 DOMAIN EXPERTISE:\n"
            context += f"{', '.join(domains)}\n\n"
        
        # Key Strengths
        strengths = self.resume_data.get('key_strengths', [])
        if strengths:
            context += "💪 KEY STRENGTHS:\n"
            for strength in strengths:
                context += f"- {strength}\n"
            context += "\n"
        
        # FAQ Context for better AI responses
        faq = self.resume_data.get('faq_responses', {})
        if faq:
            context += "=== QUICK REFERENCE FOR COMMON QUESTIONS ===\n"
            for question, answer in faq.items():
                context += f"\n{question.replace('_', ' ').title()}:\n{answer}\n"
        
        return context


# Singleton instance
resume_service = ResumeService()
