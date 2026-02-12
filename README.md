# AI-Powered Portfolio Website

A modern, responsive portfolio website with integrated AI chat functionality.

## Features

- 🎨 Modern dark theme with glassmorphism effects
- 💬 AI-powered chat assistant using OpenRouter
- 📱 Fully responsive design
- ⚡ Fast and optimized with React + Vite
- 🗄️ Supabase backend for data management
- 🤖 Context-aware AI responses based on resume data

## Tech Stack

### Frontend
- React 18 with TypeScript
- Vite for build tooling
- Modern CSS with animations

### Backend
- Python 3.12
- FastAPI
- Supabase (PostgreSQL)
- OpenRouter AI API

## Project Structure

```
AI_chat/
├── frontend/                 # React TypeScript app
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── services/        # API services
│   │   ├── types/           # TypeScript types
│   │   └── App.tsx
│   └── package.json
├── backend/                  # Python FastAPI app
│   ├── app/
│   │   ├── api/             # API routes
│   │   ├── models/          # Data models
│   │   ├── services/        # Business logic
│   │   └── main.py
│   ├── requirements.txt
│   └── database_schema.sql
└── README.md
```

## Setup Instructions

### Prerequisites
- Node.js 16+ and npm
- Python 3.8+
- Supabase account (free tier)
- OpenRouter account (free tier)

### Backend Setup

1. **Create Supabase Project**
   - Go to https://supabase.com and sign up
   - Create a new project
   - Go to SQL Editor and run the SQL from `backend/database_schema.sql`
   - Get your project URL and anon key from Settings > API

2. **Create OpenRouter Account**
   - Go to https://openrouter.ai and sign up
   - Get your API key from the dashboard

3. **Configure Backend**
   ```bash
   cd backend
   
   # Create virtual environment (optional but recommended)
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On Mac/Linux
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Create .env file
   copy .env.example .env  # On Windows
   # cp .env.example .env  # On Mac/Linux
   ```

4. **Edit .env file** with your credentials:
   ```
   SUPABASE_URL=your_supabase_project_url
   SUPABASE_KEY=your_supabase_anon_key
   OPENROUTER_API_KEY=your_openrouter_api_key
   FRONTEND_URL=http://localhost:5173
   ```

5. **Run Backend**
   ```bash
   uvicorn app.main:app --reload
   ```
   Backend will run on http://localhost:8000

### Frontend Setup

1. **Install Dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Run Frontend**
   ```bash
   npm run dev
   ```
   Frontend will run on http://localhost:5173

## Adding Your Personal Information

1. **Update Database**
   - Go to your Supabase project dashboard
   - Navigate to Table Editor
   - Update the `profiles`, `experiences`, `projects`, and `skills` tables with your information

2. **Test the Chat**
   - Open the website
   - Click the AI chat button in the bottom right
   - Ask questions about your resume!

## Available Scripts

### Frontend
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

### Backend
- `uvicorn app.main:app --reload` - Start development server
- `uvicorn app.main:app` - Start production server

## API Endpoints

- `GET /api/profile` - Get profile information
- `GET /api/experiences` - Get work experiences
- `GET /api/projects` - Get projects
- `GET /api/skills` - Get skills
- `POST /api/chat` - Send chat message

## Customization

### Colors
Edit CSS variables in `frontend/src/index.css`:
```css
:root {
  --primary: #6366f1;
  --secondary: #ec4899;
  --accent: #14b8a6;
  /* ... */
}
```

### AI Model
Change the model in `backend/app/services/chat_service.py`:
```python
self.model = "meta-llama/llama-3.1-8b-instruct:free"
```

## Deployment

### Frontend (Vercel/Netlify)
1. Build the frontend: `npm run build`
2. Deploy the `dist` folder

### Backend (Railway/Render)
1. Deploy the `backend` folder
2. Set environment variables
3. Update CORS settings in `backend/app/main.py`

## License

MIT License - feel free to use this for your own portfolio!

## Support

For issues or questions, please open an issue on GitHub.
