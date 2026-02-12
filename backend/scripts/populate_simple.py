"""
Simplified script to populate Supabase with minimal resume data
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database import get_supabase


def load_resume_data():
    """Load resume data from JSON"""
    json_path = Path(__file__).parent.parent / "data" / "resume_knowledge.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def populate_database():
    """Populate database with resume data"""
    print("🚀 Starting simplified database population...")
    print("=" * 60)
    
    try:
        data = load_resume_data()
        supabase = get_supabase()
        
        # 1. Populate Profile
        print("\n📝 Populating Profile...")
        personal = data.get('personal_info', {})
        education = data.get('education', {}).get('current', {})
        
        profile = {
            'name': personal.get('name', ''),
            'title': 'Information Technology Student',
            'bio': f"Final-year B.Tech IT student at {education.get('institution', '')} with CGPA {education.get('cgpa', '')}. Specializing in Full Stack Development, IoT, and AI.",
            'email': personal.get('email', ''),
            'phone': personal.get('phone', ''),
            'location': personal.get('location', ''),
            'linkedin': personal.get('linkedin', ''),
            'github': personal.get('github', '')
        }
        
        try:
            # Clear existing
            supabase.table('profiles').delete().gte('id', 0).execute()
        except:
            pass
        
        result = supabase.table('profiles').insert(profile).execute()
        print(f"✅ Profile inserted: {profile['name']}")
        
        # 2. Populate Projects
        print("\n🚀 Populating Projects...")
        projects = data.get('projects', [])
        
        try:
            supabase.table('projects').delete().gte('id', 0).execute()
        except:
            pass
        
        for proj in projects:
            project_data = {
                'title': proj.get('name', ''),
                'description': proj.get('description', ''),
                'technologies': proj.get('technologies', [])
            }
            supabase.table('projects').insert(project_data).execute()
            print(f"✅ Project inserted: {project_data['title']}")
        
        # 3. Populate Skills
        print("\n🛠️ Populating Skills...")
        skills = data.get('technical_skills', {})
        
        try:
            supabase.table('skills').delete().gte('id', 0).execute()
        except:
            pass
        
        category_map = {
            'programming_languages': 'Programming Languages',
            'web_technologies': 'Web Technologies',
            'databases': 'Databases',
            'soft_skills': 'Soft Skills'
        }
        
        for key, skill_list in skills.items():
            if isinstance(skill_list, list):
                category = category_map.get(key, key.replace('_', ' ').title())
                for skill_name in skill_list:
                    skill_data = {
                        'name': skill_name,
                        'category': category
                    }
                    supabase.table('skills').insert(skill_data).execute()
                    print(f"✅ Skill inserted: {skill_name}")
        
        # 4. Populate Experience
        print("\n💼 Populating Experience...")
        internship = data.get('internship', {})
        
        if internship:
            try:
                supabase.table('experiences').delete().gte('id', 0).execute()
            except:
                pass
            
            exp_data = {
                'company': internship.get('company', ''),
                'position': internship.get('role', ''),
                'location': internship.get('location', ''),
                'description': '\n'.join(internship.get('responsibilities', []))
            }
            supabase.table('experiences').insert(exp_data).execute()
            print(f"✅ Experience inserted: {exp_data['position']}")
        
        print("\n" + "=" * 60)
        print("✅ Database population completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    populate_database()
