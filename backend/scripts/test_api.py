"""
Test API endpoint to check if image URLs are being returned
"""
import requests

try:
    response = requests.get('http://localhost:8000/api/projects')
    projects = response.json()
    
    print("=" * 60)
    print("API RESPONSE - Projects:")
    print("=" * 60)
    
    for project in projects:
        print(f"\nTitle: {project.get('title', 'N/A')}")
        print(f"Image URL: {project.get('image_url', 'NULL')}")
        print(f"Has image_url key: {'image_url' in project}")
        print("-" * 60)
    
    print(f"\nTotal projects returned: {len(projects)}")
    
except Exception as e:
    print(f"Error: {e}")
