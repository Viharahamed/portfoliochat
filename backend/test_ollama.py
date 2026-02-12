import asyncio
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma2:2b")

async def test_ollama():
    print(f"Testing Ollama at: {OLLAMA_URL}")
    print(f"Using model: {OLLAMA_MODEL}")
    
    try:
        # Test 1: Check if Ollama is running
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{OLLAMA_URL}/api/tags")
            print(f"\n✓ Ollama is running!")
            print(f"Available models: {[model['name'] for model in response.json()['models']]}")
        
        # Test 2: Test chat endpoint
        print(f"\nTesting chat with model '{OLLAMA_MODEL}'...")
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{OLLAMA_URL}/api/chat",
                json={
                    "model": OLLAMA_MODEL,
                    "messages": [{"role": "user", "content": "Say hello in one sentence."}],
                    "stream": False
                }
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"✓ Chat test successful!")
                print(f"Response: {data['message']['content']}")
            else:
                print(f"✗ Chat test failed: {response.status_code}")
                print(f"Error: {response.text}")
                
    except httpx.ConnectError:
        print(f"\n✗ Cannot connect to Ollama at {OLLAMA_URL}")
        print("Make sure Ollama is running. Start it with: ollama serve")
    except Exception as e:
        print(f"\n✗ Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_ollama())
