-- Create profiles table
CREATE TABLE IF NOT EXISTS profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    title TEXT NOT NULL,
    bio TEXT,
    email TEXT,
    phone TEXT,
    location TEXT,
    linkedin TEXT,
    github TEXT,
    website TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create experiences table
CREATE TABLE IF NOT EXISTS experiences (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    profile_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
    company TEXT NOT NULL,
    position TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    description TEXT,
    technologies TEXT[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create projects table
CREATE TABLE IF NOT EXISTS projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    profile_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    technologies TEXT[],
    github_url TEXT,
    live_url TEXT,
    image_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create skills table
CREATE TABLE IF NOT EXISTS skills (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    profile_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
    category TEXT NOT NULL,
    name TEXT NOT NULL,
    proficiency TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create chat_history table
CREATE TABLE IF NOT EXISTS chat_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id TEXT NOT NULL,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_experiences_profile_id ON experiences(profile_id);
CREATE INDEX IF NOT EXISTS idx_projects_profile_id ON projects(profile_id);
CREATE INDEX IF NOT EXISTS idx_skills_profile_id ON skills(profile_id);
CREATE INDEX IF NOT EXISTS idx_chat_history_session_id ON chat_history(session_id);
CREATE INDEX IF NOT EXISTS idx_chat_history_created_at ON chat_history(created_at);

-- Insert sample profile data (you'll replace this with your actual data)
INSERT INTO profiles (name, title, bio, email, location, github, linkedin)
VALUES (
    'Your Name',
    'Full Stack Developer',
    'Passionate full-stack developer with expertise in React, Python, and modern web technologies. Love building scalable applications and solving complex problems.',
    'your.email@example.com',
    'Your City, Country',
    'https://github.com/yourusername',
    'https://linkedin.com/in/yourusername'
) ON CONFLICT DO NOTHING;

-- Get the profile ID for sample data
DO $$
DECLARE
    profile_uuid UUID;
BEGIN
    SELECT id INTO profile_uuid FROM profiles LIMIT 1;
    
    -- Insert sample experience
    INSERT INTO experiences (profile_id, company, position, start_date, end_date, description, technologies)
    VALUES (
        profile_uuid,
        'Tech Company',
        'Senior Full Stack Developer',
        '2022-01-01',
        NULL,
        'Led development of web applications using React and Python. Implemented CI/CD pipelines and improved system performance.',
        ARRAY['React', 'TypeScript', 'Python', 'FastAPI', 'PostgreSQL']
    ) ON CONFLICT DO NOTHING;
    
    -- Insert sample project
    INSERT INTO projects (profile_id, title, description, technologies, github_url)
    VALUES (
        profile_uuid,
        'AI Portfolio Website',
        'Personal portfolio with integrated AI chat functionality powered by OpenRouter',
        ARRAY['React', 'TypeScript', 'Python', 'FastAPI', 'Supabase'],
        'https://github.com/yourusername/portfolio'
    ) ON CONFLICT DO NOTHING;
    
    -- Insert sample skills
    INSERT INTO skills (profile_id, category, name, proficiency)
    VALUES 
        (profile_uuid, 'Frontend', 'React', 'Advanced'),
        (profile_uuid, 'Frontend', 'TypeScript', 'Advanced'),
        (profile_uuid, 'Frontend', 'HTML/CSS', 'Advanced'),
        (profile_uuid, 'Backend', 'Python', 'Advanced'),
        (profile_uuid, 'Backend', 'FastAPI', 'Intermediate'),
        (profile_uuid, 'Database', 'PostgreSQL', 'Intermediate'),
        (profile_uuid, 'Database', 'Supabase', 'Intermediate'),
        (profile_uuid, 'Tools', 'Git', 'Advanced'),
        (profile_uuid, 'Tools', 'Docker', 'Intermediate')
    ON CONFLICT DO NOTHING;
END $$;
