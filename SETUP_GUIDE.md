# AI Portfolio Website - Step-by-Step Setup Guide

## 🎯 What We've Built

I've created a complete AI-powered portfolio website with:
- ✅ React TypeScript frontend with modern design
- ✅ Python FastAPI backend
- ✅ AI chat functionality using OpenRouter
- ✅ Supabase database integration
- ✅ Responsive, professional design with animations

---

## 📋 Next Steps - What YOU Need to Do

### Step 1: Create Supabase Account (5 minutes)

**What to do:**
1. Go to https://supabase.com
2. Click "Start your project"
3. Sign up with GitHub or email
4. Click "New Project"
5. Fill in:
   - **Name**: `portfolio-ai` (or any name you like)
   - **Database Password**: Create a strong password (SAVE THIS!)
   - **Region**: Choose closest to you
   - **Plan**: Free
6. Click "Create new project"
7. Wait 2-3 minutes for setup to complete

**What you'll get:**
- Project URL (looks like: `https://xxxxx.supabase.co`)
- Anon/Public key (long string starting with `eyJ...`)

---

### Step 2: Set Up Database Tables (3 minutes)

**What to do:**
1. In your Supabase project, click "SQL Editor" in the left sidebar
2. Click "New Query"
3. Open the file: `backend/database_schema.sql` (I created this)
4. Copy ALL the SQL code from that file
5. Paste it into the Supabase SQL Editor
6. Click "Run" button (bottom right)
7. You should see "Success. No rows returned"

**What this does:**
- Creates tables for your profile, experience, projects, skills, and chat history
- Adds sample data so you can test immediately

---

### Step 3: Create OpenRouter Account (3 minutes)

**What to do:**
1. Go to https://openrouter.ai
2. Click "Sign In" (top right)
3. Sign up with Google or email
4. After logging in, click your profile icon
5. Click "Keys"
6. Click "Create Key"
7. Give it a name like "Portfolio Chat"
8. Click "Create"
9. **COPY THE KEY** (starts with `sk-or-...`) - you won't see it again!

**What you'll get:**
- API key for free AI chat (no credit card needed for free models)

---

### Step 4: Configure Backend (5 minutes)

**What to do:**
1. Open your terminal/command prompt
2. Navigate to the backend folder:
   ```bash
   cd c:\Users\vihar\Music\Projects\Portfolio\AI_chat\backend
   ```

3. Create a `.env` file by copying the example:
   ```bash
   copy .env.example .env
   ```

4. Open the `.env` file in any text editor (Notepad, VS Code, etc.)

5. Replace the placeholder values with your actual credentials:
   ```
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   OPENROUTER_API_KEY=sk-or-v1-...
   FRONTEND_URL=http://localhost:5173
   ```

6. Save the file

---

### Step 5: Install Backend Dependencies (2 minutes)

**What to do:**
1. In the terminal (still in the backend folder):
   ```bash
   pip install -r requirements.txt
   ```

2. Wait for installation to complete (you'll see "Successfully installed...")

**If you get an error:**
- Make sure Python is in your PATH
- Try: `python -m pip install -r requirements.txt`

---

### Step 6: Run the Backend (1 minute)

**What to do:**
1. In the terminal (backend folder):
   ```bash
   uvicorn app.main:app --reload
   ```

2. You should see:
   ```
   INFO:     Uvicorn running on http://127.0.0.1:8000
   INFO:     Application startup complete.
   ```

3. **Keep this terminal window open!** The backend needs to stay running.

4. Test it: Open http://localhost:8000 in your browser
   - You should see: `{"message":"Portfolio AI Chat API","version":"1.0.0","status":"running"}`

---

### Step 7: Run the Frontend (1 minute)

**What to do:**
1. Open a **NEW** terminal window (keep the backend running!)
2. Navigate to frontend:
   ```bash
   cd c:\Users\vihar\Music\Projects\Portfolio\AI_chat\frontend
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. You should see:
   ```
   VITE v5.x.x  ready in xxx ms
   ➜  Local:   http://localhost:5173/
   ```

5. Open http://localhost:5173 in your browser

---

### Step 8: Test Everything! (5 minutes)

**What to test:**

1. **Portfolio Sections**
   - ✅ Hero section shows "Your Name" and title
   - ✅ Experience section shows timeline
   - ✅ Projects section shows project cards
   - ✅ Skills section shows categorized skills
   - ✅ Contact section shows contact info

2. **AI Chat**
   - ✅ Click the floating AI button (bottom right)
   - ✅ Chat window opens
   - ✅ Type: "What skills does this person have?"
   - ✅ AI responds with information from the database
   - ✅ Try: "Tell me about their work experience"
   - ✅ Try: "What projects have they built?"

3. **Responsive Design**
   - ✅ Resize browser window
   - ✅ Check mobile view (press F12, click device icon)

---

### Step 9: Add Your Personal Information (10 minutes)

**What to do:**

1. Go to your Supabase project dashboard
2. Click "Table Editor" in the left sidebar
3. Update each table with YOUR information:

**Profiles Table:**
- Click on the row
- Edit: name, title, bio, email, location, github, linkedin
- Click "Save"

**Experiences Table:**
- Click "Insert" → "Insert row"
- Fill in your work experience
- Add multiple rows for each job

**Projects Table:**
- Click "Insert" → "Insert row"
- Add your projects
- Include GitHub URLs and descriptions

**Skills Table:**
- Click "Insert" → "Insert row"
- Add your skills by category
- Categories: Frontend, Backend, Database, Tools, etc.

4. Refresh your portfolio website
5. Test the AI chat again - it should now know YOUR information!

---

## 🎨 Customization (Optional)

### Change Colors
Edit `frontend/src/index.css`:
```css
:root {
  --primary: #6366f1;      /* Main color */
  --secondary: #ec4899;    /* Accent color */
  --accent: #14b8a6;       /* Highlight color */
}
```

### Change AI Model
Edit `backend/app/services/chat_service.py` line 18:
```python
self.model = "meta-llama/llama-3.1-8b-instruct:free"
```
See other free models at: https://openrouter.ai/models?order=newest&supported_parameters=tools&max_price=0

---

## ❓ Troubleshooting

### Backend won't start
- Check if `.env` file exists and has correct values
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check if port 8000 is already in use

### Frontend shows errors
- Make sure backend is running on port 8000
- Check browser console (F12) for error messages
- Verify API URL in `frontend/src/services/api.ts`

### AI chat not working
- Verify OpenRouter API key is correct
- Check backend terminal for error messages
- Make sure you have internet connection
- Try a different free model

### Database connection fails
- Verify Supabase URL and key in `.env`
- Check if database tables were created (Step 2)
- Make sure Supabase project is active

---

## 🚀 What's Next?

1. **Add your information** to the database
2. **Test the AI chat** thoroughly
3. **Customize the design** to match your style
4. **Add more projects** and experiences
5. **Deploy to production** (Vercel for frontend, Railway for backend)

---

## 📞 Need Help?

If you encounter any issues:
1. Check the error message in the terminal
2. Look at the browser console (F12)
3. Verify all environment variables are set correctly
4. Make sure both backend and frontend are running

Let me know what step you're on and I'll help you through it!
