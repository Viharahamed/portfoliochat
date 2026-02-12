
import asyncio
import os
from dotenv import load_dotenv
import httpx
import traceback

# Load environment variables
if os.path.exists('.env'):
    load_dotenv('.env')
elif os.path.exists('backend/.env'):
    load_dotenv('backend/.env')

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

async def check_openrouter():
    print(f"API Key present: {bool(OPENROUTER_API_KEY)}")
    print(f"API Key length: {len(OPENROUTER_API_KEY) if OPENROUTER_API_KEY else 0}")
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5173",
        "X-Title": "Portfolio AI Chat"
    }
    data = {
        "model": "google/gemma-7b-it:free",
        "messages": [{"role": "user", "content": "Hello"}],
    }

    print(f"Sending request to {url}...")
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(url, headers=headers, json=data)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
            response.raise_for_status()
            print("✅ Success!")
    except Exception as e:
        print(f"❌ Error: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(check_openrouter())
