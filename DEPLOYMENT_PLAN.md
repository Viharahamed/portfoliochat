# Portfolio Deployment Plan

This document outlines the deployment strategy for your full-stack portfolio application.

---

## 🎯 Deployment Strategy

**Backend**: Render.com (Free tier)  
**Frontend**: Vercel (Free tier)

---

## ⚠️ Important Considerations

### Ollama Service Issue

Your backend currently uses **Ollama** for AI chat functionality. However, **Render's free tier doesn't support running Ollama**.

**You have two options:**

1. **Switch to a cloud AI service** (Recommended):
   - [OpenRouter](https://openrouter.ai) - Supports multiple models including Gemma
   - [OpenAI API](https://platform.openai.com) - Industry standard
   - Requires updating backend code to use these APIs instead of Ollama

2. **Deploy Ollama separately**:
   - Use [Railway](https://railway.app) or [Fly.io](https://fly.io) (both support Docker)
   - Update `OLLAMA_URL` environment variable to point to that service
   - Additional cost and complexity

**For now, I'll proceed with the deployment setup. The chat feature won't work until you implement one of these options.**

---

## 📦 What I've Prepared

### Configuration Files Created

1. **`render.yaml`** - Backend deployment configuration
   - Defines Python web service
   - Specifies build/start commands
   - Lists environment variables

2. **`frontend/vercel.json`** - Frontend deployment configuration
   - Configures Vite build
   - Sets up SPA routing

3. **`frontend/.env.production`** - Production environment variables
   - Template for backend API URL
   - **You'll need to update this after deploying backend**

4. **`frontend/.env.development`** - Development environment variables
   - Points to localhost for local development

### Code Changes

1. **`frontend/src/services/api.ts`**
   - Updated to use environment variable for API URL
   - Falls back to localhost for development

2. **`frontend/.gitignore`**
   - Added `.env` files to prevent committing secrets

### Documentation

1. **`DEPLOYMENT_GUIDE.md`** - Comprehensive step-by-step guide
   - Backend deployment instructions
   - Frontend deployment instructions
   - Troubleshooting tips
   - Environment variable setup

2. **`DEPLOYMENT_TASKS.md`** - Task checklist
   - Track deployment progress

---

## 🚀 Next Steps (Your Action Required)

### Step 1: Review & Commit Changes

```bash
# Review the changes
git status
git diff

# Add all deployment files
git add .

# Commit changes
git commit -m "Add deployment configuration for Render and Vercel"

# Push to GitHub
git push origin main
```

### Step 2: Deploy Backend to Render

Follow the detailed instructions in [`DEPLOYMENT_GUIDE.md`](file:///c:/Users/vihar/Music/Projects/Portfolio/AI_chat/DEPLOYMENT_GUIDE.md) - Part 1

**Quick summary:**
1. Go to [render.com](https://render.com) and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Render will detect `render.yaml` automatically
5. Add environment variables:
   - `SUPABASE_URL`
   - `SUPABASE_KEY`
   - `OLLAMA_URL` (placeholder for now)
   - `OLLAMA_MODEL`
   - `FRONTEND_URL` (will update after Vercel deployment)
6. Deploy and **copy your backend URL**

### Step 3: Update Frontend Environment

Edit `frontend/.env.production`:
```env
VITE_API_URL=https://your-backend-url.onrender.com
```

**Commit and push this change:**
```bash
git add frontend/.env.production
git commit -m "Update production API URL"
git push origin main
```

### Step 4: Deploy Frontend to Vercel

Follow [`DEPLOYMENT_GUIDE.md`](file:///c:/Users/vihar/Music/Projects/Portfolio/AI_chat/DEPLOYMENT_GUIDE.md) - Part 2

**Quick summary:**
1. Go to [vercel.com](https://vercel.com) and sign up
2. Click "Add New Project"
3. Import your GitHub repository
4. Configure:
   - **Framework**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
5. Add environment variable:
   - Key: `VITE_API_URL`
   - Value: Your Render backend URL
6. Deploy and **copy your Vercel URL**

### Step 5: Update Backend CORS

1. Go back to Render dashboard
2. Update `FRONTEND_URL` environment variable with your Vercel URL
3. Trigger a redeploy

### Step 6: Verify Deployment

1. Visit your Vercel URL
2. Check all sections load (About, Experience, Projects, Skills, Contact)
3. Open browser DevTools → Network tab
4. Verify API calls go to your Render backend
5. Check for any errors in console

---

## 🔧 Troubleshooting

If you encounter issues, check:
- Render logs (in Render dashboard)
- Vercel deployment logs
- Browser console for errors
- Environment variables are set correctly

See [`DEPLOYMENT_GUIDE.md`](file:///c:/Users/vihar/Music/Projects/Portfolio/AI_chat/DEPLOYMENT_GUIDE.md) for detailed troubleshooting.

---

## 📝 Summary

All configuration files are ready. You just need to:
1. ✅ Commit and push to GitHub
2. ✅ Deploy backend to Render
3. ✅ Update `.env.production` with backend URL
4. ✅ Deploy frontend to Vercel
5. ✅ Update backend CORS settings
6. ✅ Verify everything works

**The deployment process should take about 15-20 minutes total.**

---

## ❓ Questions?

- **Which Ollama alternative do you prefer?** (OpenRouter, OpenAI, or separate deployment)
- **Do you need help with any specific step?**
- **Would you like me to help update the backend code for a cloud AI service?**
