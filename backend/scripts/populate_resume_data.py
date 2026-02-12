"""
Script to populate Supabase database with resume data from resume_knowledge.json
Run this script to insert all resume information into the database tables.
"""

import json
import sys
from pathlib import Path

# Add parent directory to path to import app modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database import get_supabase


def load_resume_data():
    """Load resume data from JSON file"""
    json_path = Path(__file__).parent.parent / "data" / "resume_knowledge.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def populate_profile(supabase, data):
    """Populate profiles table"""
    personal_info = data.get('personal_info', {})
    education = data.get('education', {}).get('current', {})
    
    profile_data = {
        'name': personal_info.get('name', ''),
        'title': 'Information Technology Student',
        'bio': f"Final-year B.Tech IT student at {education.get('institution', '')} with CGPA {education.get('cgpa', '')}. Specializing in Full Stack Development, IoT Applications, and AI-driven Analytics.",
        'email': personal_info.get('email', ''),
        'phone': personal_info.get('phone', ''),
        'location': personal_info.get('location', ''),
        'linkedin': personal_info.get('linkedin', ''),
        'github': personal_info.get('github', '')
    }
    
    # Delete existing profile
    supabase.table('profiles').delete().neq('id', '00000000-0000-0000-0000-000000000000').execute()
    
    # Insert new profile
    result = supabase.table('profiles').insert(profile_data).execute()
    print(f"✅ Inserted profile: {profile_data['name']}")
    return result


def populate_experiences(supabase, data):
    """Populate experiences table"""
    internship = data.get('internship', {})
    
    if not internship:
        print("⚠️ No internship data found")
        return
    
    experience_data = {
        'company': internship.get('company', ''),
        'position': internship.get('role', ''),
        'location': internship.get('location', ''),
        'start_date': '2025-06-01',  # Extracted from "June 2025"
        'end_date': '2025-06-30',
        'description': '\n'.join(internship.get('responsibilities', [])),
        'technologies': internship.get('technologies_used', [])
    }
    
    # Delete existing experiences
    supabase.table('experiences').delete().neq('id', '00000000-0000-0000-0000-000000000000').execute()
    
    # Insert new experience
    result = supabase.table('experiences').insert(experience_data).execute()
    print(f"✅ Inserted experience: {experience_data['position']} at {experience_data['company']}")
    return result


def populate_projects(supabase, data):
    """Populate projects table"""
    projects = data.get('projects', [])
    
    if not projects:
        print("⚠️ No projects data found")
        return
    
    # Delete existing projects
    supabase.table('projects').delete().neq('id', '00000000-0000-0000-0000-000000000000').execute()
    
    for project in projects:
        project_data = {
            'title': project.get('name', ''),
            'description': project.get('description', ''),
            'technologies': project.get('technologies', []),
            'github_url': '',  # Not in resume
            'live_url': '',    # Not in resume
            'image_url': '',   # Not in resume
            'featured': True
        }
        
        result = supabase.table('projects').insert(project_data).execute()
        print(f"✅ Inserted project: {project_data['title']}")


def populate_skills(supabase, data):
    """Populate skills table"""
    technical_skills = data.get('technical_skills', {})
    
    if not technical_skills:
        print("⚠️ No skills data found")
        return
    
    # Delete existing skills
    supabase.table('skills').delete().neq('id', '00000000-0000-0000-0000-000000000000').execute()
    
    # Map JSON categories to database categories
    category_mapping = {
        'programming_languages': 'Programming Languages',
        'web_technologies': 'Web Technologies',
        'databases': 'Databases',
        'soft_skills': 'Soft Skills'
    }
    
    for json_category, skill_list in technical_skills.items():
        if not isinstance(skill_list, list):
            continue
            
        category = category_mapping.get(json_category, json_category.replace('_', ' ').title())
        
        for skill_name in skill_list:
            skill_data = {
                'name': skill_name,
                'category': category,
                'proficiency': 'Advanced' if json_category == 'programming_languages' else 'Intermediate'
            }
            
            result = supabase.table('skills').insert(skill_data).execute()
            print(f"✅ Inserted skill: {skill_name} ({category})")


def main():
    """Main function to populate all tables"""
    print("🚀 Starting database population...")
    print("=" * 60)
    
    try:
        # Load resume data
        print("\n📖 Loading resume data from JSON...")
        data = load_resume_data()
        print(f"✅ Loaded resume data for: {data.get('personal_info', {}).get('name', 'Unknown')}")
        
        # Get Supabase client
        print("\n🔌 Connecting to Supabase...")
        supabase = get_supabase()
        print("✅ Connected to Supabase")
        
        # Populate tables
        print("\n📝 Populating Profile...")
        populate_profile(supabase, data)
        
        print("\n💼 Populating Experiences...")
        populate_experiences(supabase, data)
        
        print("\n🚀 Populating Projects...")
        populate_projects(supabase, data)
        
        print("\n🛠️ Populating Skills...")
        populate_skills(supabase, data)
        
        print("\n" + "=" * 60)
        print("✅ Database population completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
