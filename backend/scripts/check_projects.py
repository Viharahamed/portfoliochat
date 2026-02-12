"""
Check project data from Supabase
"""
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# Get all projects
response = supabase.table('projects').select('*').execute()

print("=" * 60)
print("PROJECTS IN DATABASE:")
print("=" * 60)

for project in response.data:
    print(f"\nTitle: {project['title']}")
    print(f"Image URL: {project.get('image_url', 'NULL')}")
    print(f"Description: {project.get('description', '')[:50]}...")
    print("-" * 60)

print(f"\nTotal projects: {len(response.data)}")
