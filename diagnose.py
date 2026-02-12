
import asyncio
import os
from dotenv import load_dotenv
from supabase import create_client, Client
import httpx

# Load environment variables
# Load environment variables
# If running from backend directory, .env is in current directory
if os.path.exists('.env'):
    load_dotenv('.env')
# If running from root directory, .env is in backend directory
elif os.path.exists('backend/.env'):
    load_dotenv('backend/.env')
else:
    print("❌ .env file not found!")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

print(f"SUPABASE_URL: {SUPABASE_URL}")
# print(f"SUPABASE_KEY: {SUPABASE_KEY}") # Don't print secrets
# print(f"OPENROUTER_API_KEY: {OPENROUTER_API_KEY}") # Don't print secrets

async def check_supabase():
    print("\n--- Checking Supabase ---")
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Check profiles table
        print("Checking 'profiles' table...")
        response = supabase.table('profiles').select('*').execute()
        print(f"Profiles count: {len(response.data)}")
        if response.data:
            print(f"First profile: {response.data[0].get('name')}")
        else:
            print("⚠️ No profiles found!")

        # Check other tables
        for table in ['experiences', 'projects', 'skills']:
            print(f"Checking '{table}' table...")
            try:
                response = supabase.table(table).select('*').limit(1).execute()
                print(f"{table} count: {len(response.data)}")
            except Exception as e:
                print(f"❌ Error checking {table}: {e}")

    except Exception as e:
        print(f"❌ Supabase Connection Error: {e}")

async def check_openrouter():
    print("\n--- Checking OpenRouter ---")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "meta-llama/llama-3.1-8b-instruct:free",
                    "messages": [{"role": "user", "content": "Hello"}],
                },
                timeout=10.0
            )
            if response.status_code == 200:
                print("✅ OpenRouter API is working!")
                print(f"Response: {response.json()['choices'][0]['message']['content'][:50]}...")
            else:
                print(f"❌ OpenRouter API Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ OpenRouter Connection Error: {e}")

async def main():
    await check_supabase()
    await check_openrouter()

if __name__ == "__main__":
    asyncio.run(main())
