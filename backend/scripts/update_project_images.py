"""
Update project image URLs in Supabase database
"""
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

def update_project_images():
    """Update project image URLs based on project titles"""
    
    # Get all projects
    response = supabase.table('projects').select('*').execute()
    projects = response.data
    
    print(f"Found {len(projects)} projects")
    
    for project in projects:
        image_url = None
        title_lower = project['title'].lower()
        
        # Match project by title and assign appropriate image
        if 'ev' in title_lower or 'tracking' in title_lower or 'vehicle' in title_lower:
            image_url = '/srec_logo.svg'
            print(f"✓ Updating '{project['title']}' with SREC logo")
        elif 'instagram' in title_lower or 'insta' in title_lower or 'social media' in title_lower or 'automated' in title_lower:
            image_url = '/instagram_icon.svg'
            print(f"✓ Updating '{project['title']}' with Instagram icon")
        
        # Update the project if image URL was determined
        if image_url:
            supabase.table('projects').update({
                'image_url': image_url
            }).eq('id', project['id']).execute()
            print(f"  → Image URL set to: {image_url}")
    
    print("\n✅ Project images updated successfully!")
    
    # Display updated projects
    print("\nUpdated projects:")
    response = supabase.table('projects').select('title, image_url').execute()
    for project in response.data:
        print(f"  • {project['title']}: {project['image_url'] or '(no image)'}")

if __name__ == "__main__":
    update_project_images()
