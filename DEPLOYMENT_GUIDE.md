# Deployment Guide

This guide will walk you through deploying your portfolio application with:
- **Backend**: Render.com (Free tier)
- **Frontend**: Vercel (Free tier)

## Prerequisites

- GitHub account
- Render.com account (create at https://render.com)
- Vercel account (create at https://vercel.com)
- Your code pushed to a GitHub repository

---

## Part 1: Deploy Backend to Render

### Step 1: Prepare Backend for Deployment

Your backend is already configured! The `render.yaml` file has been created with the necessary settings.

### Step 2: Create Render Account & Deploy

1. Go to https://render.com and sign up/login
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Render will auto-detect the `render.yaml` configuration
5. Click **"Apply"** to use the blueprint

### Step 3: Configure Environment Variables

In the Render dashboard, add these environment variables:

```
SUPABASE_URL=https://kaqvrdiepelgakibasnw.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImthcXZyZGllcGVsZ2FraWJhc253Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzA3ODIwNjMsImV4cCI6MjA4NjM1ODA2M30.FiJaDroGtp_vFffdBTJZzH-LyF8GZej6yyNmJSGk8JY
OLLAMA_URL=https://your-ollama-service-url.com
OLLAMA_MODEL=gemma2:2b
FRONTEND_URL=https://your-vercel-app.vercel.app
```

> **Note**: You'll need to update `FRONTEND_URL` after deploying the frontend in Part 2.
> **Important**: For Ollama, you'll need to deploy it separately or use an alternative AI service since Render's free tier doesn't support Ollama. Consider using OpenRouter or OpenAI API instead.

### Step 4: Deploy

1. Click **"Create Web Service"**
2. Wait for the build to complete (5-10 minutes)
3. Once deployed, copy your backend URL (e.g., `https://your-app.onrender.com`)

---

## Part 2: Deploy Frontend to Vercel

### Step 1: Prepare Frontend for Deployment

The configuration files have been created:
- `vercel.json` - Vercel deployment settings
- `.env.production` - Production environment variables

### Step 2: Update Environment Variables

Edit `frontend/.env.production` and replace `YOUR_RENDER_BACKEND_URL` with your actual Render backend URL from Part 1:

```
VITE_API_URL=https://your-app.onrender.com
```

### Step 3: Deploy to Vercel

#### Option A: Using Vercel Dashboard (Recommended)

1. Go to https://vercel.com and sign up/login
2. Click **"Add New Project"**
3. Import your GitHub repository
4. Configure project settings:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
5. Add environment variable:
   - Key: `VITE_API_URL`
   - Value: Your Render backend URL (e.g., `https://your-app.onrender.com`)
6. Click **"Deploy"**

#### Option B: Using Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Navigate to frontend directory
cd frontend

# Deploy
vercel

# Follow the prompts:
# - Set up and deploy? Yes
# - Which scope? (select your account)
# - Link to existing project? No
# - Project name? (accept default or customize)
# - Directory? ./
# - Override settings? No

# For production deployment
vercel --prod
```

### Step 4: Get Your Frontend URL

After deployment completes, Vercel will provide your app URL (e.g., `https://your-app.vercel.app`)

### Step 5: Update Backend CORS Settings

Go back to Render dashboard and update the `FRONTEND_URL` environment variable with your Vercel URL:

```
FRONTEND_URL=https://your-app.vercel.app
```

Then trigger a redeploy of your backend service.

---

## Part 3: Verification

### Test Your Deployment

1. Visit your Vercel frontend URL
2. Check that the portfolio loads correctly
3. Test the chat functionality
4. Verify all sections (About, Experience, Projects, Skills, Contact) load properly

### Common Issues

#### Backend Issues
- **Build fails**: Check that `requirements.txt` is correct
- **Service won't start**: Verify environment variables are set
- **CORS errors**: Ensure `FRONTEND_URL` matches your Vercel domain exactly

#### Frontend Issues
- **API calls fail**: Verify `VITE_API_URL` is set correctly in Vercel
- **404 errors**: Check that `vercel.json` routing is configured
- **Build fails**: Ensure all dependencies are in `package.json`

### Monitoring

- **Render**: Check logs in the Render dashboard under "Logs" tab
- **Vercel**: Check deployment logs and runtime logs in Vercel dashboard

---

## Important Notes

### Ollama Limitation

The free tier of Render doesn't support running Ollama. You have two options:

1. **Use a cloud AI service** (Recommended):
   - OpenRouter (https://openrouter.ai)
   - OpenAI API (https://platform.openai.com)
   - Update your backend code to use these services instead

2. **Deploy Ollama separately**:
   - Use a service that supports Docker (Railway, Fly.io)
   - Update `OLLAMA_URL` to point to that service

### Free Tier Limitations

- **Render Free Tier**: 
  - Service spins down after 15 minutes of inactivity
  - First request after spin-down takes 30-60 seconds
  - 750 hours/month of runtime

- **Vercel Free Tier**:
  - 100 GB bandwidth/month
  - Unlimited deployments
  - Automatic HTTPS

### Keeping Services Active

To prevent Render from spinning down:
- Use a service like UptimeRobot (https://uptimerobot.com) to ping your backend every 10 minutes
- Note: This may violate Render's free tier terms of service

---

## Next Steps

1. Set up custom domain (optional)
2. Configure environment-specific settings
3. Set up monitoring and analytics
4. Configure CI/CD for automatic deployments

## Support

If you encounter issues:
- Check Render logs for backend errors
- Check Vercel deployment logs for frontend errors
- Verify all environment variables are set correctly
- Ensure your GitHub repository is up to date
