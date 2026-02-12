
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
if os.path.exists('.env'):
    load_dotenv('.env')
elif os.path.exists('backend/.env'):
    load_dotenv('backend/.env')

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ Error: Supabase credentials not found in .env")
    exit(1)

try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception as e:
    print(f"❌ Error creating Supabase client: {e}")
    exit(1)

# Resume Data
PROFILE_DATA = {
    "name": "Viharahamed M",
    "title": "Information Technology Student / Full Stack Developer",
    "bio": "Bachelor of Technology - Information Technology student at Sri Ramakrishna Engineering College (2027 Expected). Passionate about building scalable full-stack applications, IoT architecture, and AI-driven solutions.",
    "email": "viharahamed2905@gmail.com",
    "phone": "+91 9080670027",
    "location": "Coimbatore, Tamil Nadu",
    "linkedin": "https://linkedin.com/in/viharahamed-m",
    "github": "https://github.com/Viharahamed",
    "website": None
}

EXPERIENCES = [
    {
        "company": "Nexoris Solutions",
        "position": "Intern",
        "start_date": "2025-06-01",  # As per resume
        "end_date": None, 
        "description": "Developed a data analytics dashboard for visualization of data with clean design. Integrated an AI-driven query assistant capable of understanding user questions and generating relevant code-based or analytical responses.",
        "technologies": ["Data Analytics", "AI", "Dashboard Design"]
    }
]

PROJECTS = [
    {
        "title": "EVTracking",
        "description": "Developed a real-time Electric Vehicle Tracking application leveraging Next.js for the frontend and Express.js on Google Cloud run for backend services. Focused on low-latency data processing, real-time communication and scalable full stack IoT architecture for multiple vehicle support and mobile integration.",
        "technologies": ["SIM7600 4GGPS module", "Node.js", "Socket.IO", "React.js", "Express.js", "Next.js", "Google Cloud Run"],
        "github_url": None,
        "live_url": None
    },
    {
        "title": "Automated Social Media Extraction and Digital Investigations",
        "description": "Developed and automated system that extracts and analyses data from Instagram public profiles to aid digital investigations. Using NLP and CNN, it performs sentiment analysis on text and images to evaluate risk levels. It collects details from the profiles storing results in structured JSON files.",
        "technologies": ["NLP", "CNN", "JSON", "Instaloader", "Transformers", "TensorFlow"],
        "github_url": None,
        "live_url": None
    }
]

SKILLS = [
    {"category": "Programming Languages", "name": "C", "proficiency": "Intermediate"},
    {"category": "Programming Languages", "name": "Java", "proficiency": "Intermediate"},
    {"category": "Web Technologies", "name": "HTML", "proficiency": "Advanced"},
    {"category": "Web Technologies", "name": "CSS", "proficiency": "Advanced"},
    {"category": "Web Technologies", "name": "Javascript", "proficiency": "Advanced"},
    {"category": "Web Technologies", "name": "React JS", "proficiency": "Advanced"},
    {"category": "Web Technologies", "name": "Node.js", "proficiency": "Intermediate"},
    {"category": "Web Technologies", "name": "Express.js", "proficiency": "Intermediate"},
    {"category": "Databases", "name": "SQL", "proficiency": "Intermediate"},
    {"category": "Databases", "name": "MongoDB", "proficiency": "Intermediate"},
    {"category": "Soft Skills", "name": "Problem Solving", "proficiency": "Advanced"},
    {"category": "Soft Skills", "name": "Leadership", "proficiency": "Advanced"},
    {"category": "Soft Skills", "name": "Communications", "proficiency": "Advanced"},
]

def update_content():
    print("🚀 Starting content update...")
    
    # 1. Get or Create Profile
    print("Processing Profile...")
    try:
        profile_res = supabase.table('profiles').select('id').limit(1).execute()
        
        if profile_res.data:
            profile_id = profile_res.data[0]['id']
            print(f"Found existing profile ID: {profile_id}")
            # Update existing
            supabase.table('profiles').update(PROFILE_DATA).eq('id', profile_id).execute()
        else:
            print("Creating new profile...")
            # Insert new
            res = supabase.table('profiles').insert(PROFILE_DATA).execute()
            profile_id = res.data[0]['id']
        
        print("✅ Profile updated.")

        # 2. Clear existing sub-tables
        print("Clearing existing experiences, projects, and skills...")
        supabase.table('experiences').delete().eq('profile_id', profile_id).execute()
        supabase.table('projects').delete().eq('profile_id', profile_id).execute()
        supabase.table('skills').delete().eq('profile_id', profile_id).execute()

        # 3. Insert Experiences
        print(f"Inserting {len(EXPERIENCES)} experiences...")
        for exp in EXPERIENCES:
            exp_data = exp.copy()
            exp_data['profile_id'] = profile_id
            supabase.table('experiences').insert(exp_data).execute()
            
        # 4. Insert Projects
        print(f"Inserting {len(PROJECTS)} projects...")
        for proj in PROJECTS:
            proj_data = proj.copy()
            proj_data['profile_id'] = profile_id
            supabase.table('projects').insert(proj_data).execute()

        # 5. Insert Skills
        print(f"Inserting {len(SKILLS)} skills...")
        for skill in SKILLS:
            skill_data = skill.copy()
            skill_data['profile_id'] = profile_id
            supabase.table('skills').insert(skill_data).execute()

        print("✨ Content update complete!")

    except Exception as e:
        print(f"❌ Error during update: {e}")
        # Print full traceback if possible
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    update_content()
