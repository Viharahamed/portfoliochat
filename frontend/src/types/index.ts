export interface Profile {
  id: string;
  name: string;
  title: string;
  bio?: string;
  email?: string;
  phone?: string;
  location?: string;
  linkedin?: string;
  github?: string;
  website?: string;
  created_at: string;
}

export interface Experience {
  id: string;
  profile_id: string;
  company: string;
  position: string;
  start_date: string;
  end_date?: string;
  description?: string;
  technologies: string[];
  created_at: string;
}

export interface Project {
  id: string;
  profile_id: string;
  title: string;
  description?: string;
  technologies: string[];
  github_url?: string;
  live_url?: string;
  image_url?: string;
  created_at: string;
}

export interface Skill {
  id: string;
  profile_id: string;
  category: string;
  name: string;
  proficiency?: string;
  created_at: string;
}

export interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
}

export interface ChatRequest {
  message: string;
  session_id?: string;
}

export interface ChatResponse {
  response: string;
  session_id: string;
}
