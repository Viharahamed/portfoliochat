import type { Profile, Experience, Project, Skill, ChatRequest, ChatResponse } from '../types';

const API_BASE_URL = 'http://localhost:8000/api';

class ApiService {
    private async fetchData<T>(endpoint: string): Promise<T> {
        const response = await fetch(`${API_BASE_URL}${endpoint}`);
        if (!response.ok) {
            throw new Error(`API Error: ${response.statusText}`);
        }
        return response.json();
    }

    async getProfile(): Promise<Profile> {
        return this.fetchData<Profile>('/profile');
    }

    async getExperiences(): Promise<Experience[]> {
        return this.fetchData<Experience[]>('/experiences');
    }

    async getProjects(): Promise<Project[]> {
        return this.fetchData<Project[]>('/projects');
    }

    async getSkills(): Promise<Skill[]> {
        return this.fetchData<Skill[]>('/skills');
    }

    async sendChatMessage(message: string, sessionId?: string): Promise<ChatResponse> {
        const response = await fetch(`${API_BASE_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message,
                session_id: sessionId,
            } as ChatRequest),
        });

        if (!response.ok) {
            throw new Error(`Chat API Error: ${response.statusText}`);
        }

        return response.json();
    }
}

export const apiService = new ApiService();
