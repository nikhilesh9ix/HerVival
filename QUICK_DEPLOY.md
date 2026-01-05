# Quick Deploy to Vercel - HerVival

## Quick Start (2 Steps)

### 1. Deploy

**Option A - Using PowerShell Script (Recommended)**
```powershell
.\deploy-to-vercel.ps1
```

**Option B - Manual Deployment**
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel --prod
```

**Option C - GitHub Integration**
1. Push your code to GitHub
2. Go to vercel.com/new
3. Import your repository
4. Vercel will deploy automatically

### 2. Test Your App

Visit your deployment URL (e.g., `https://hervival.vercel.app`)

## Files Created for Deployment

- ✅ `vercel.json` - Vercel configuration
- ✅ `.vercelignore` - Files to exclude
- ✅ `requirements.vercel.txt` - Optimized dependencies
- ✅ `deploy-to-vercel.ps1` - Automated deployment script
- ✅ Modified `app.py` - Added WSGI application variable

## Important Notes

**Authentication Removed**: The app now runs without authentication. Anyone can access all pages directly.

### Why requirements.vercel.txt?

Your original `requirements.txt` includes heavy ML libraries (`transformers`, `torch`) that aren't actually used in your code. The optimized version only includes what you need:

- flask==3.0.0
- python-dotenv==1.0.0
- flask-cors==5.0.1
- requests==2.31.0

This reduces deployment size and improves cold start times.

### Firebase Configuration

After deployment, update your Firebase project settings:
1. Go to Firebase Console
2. Project Settings → Authorized domains
3. Add your Vercel domain (e.g., `hervival.vercel.app`)

### Custom Domain (Optional)

To add a custom domain:
1. Vercel Dashboard → Your Project → Settings → Domains
2. Add your domain and follow DNS instructions

## Troubleshooting

**Deployment fails with size error:**
- Make sure you're using `requirements.vercel.txt` (deployment script handles this)

**Environment variables not working:**
- Verify all variables are set in Vercel Dashboard
- Redeploy after adding variables

**404 errors on routes:**
- Clear browser cache
- Check `vercel.json` routes configuration

**Firebase authentication not working:**
- Verify Vercel domain is whitelisted in Firebase
- Check that all Firebase env variables are set correctly

## Getting Help

- Vercel Docs: https://vercel.com/docs
- Vercel Support: https://vercel.com/support
- Check deployment logs in Vercel Dashboard

## Deployment Checklist

- [ ] Environment variables set in Vercel
- [ ] Code pushed to repository (if using GitHub)
- [ ] Deployment completed successfully
- [ ] App accessible at Vercel URL
- [ ] Firebase domain whitelisted
- [ ] Authentication tested
- [ ] Chat functionality tested
- [ ] Emergency services page tested
- [ ] Counselors page tested

🎉 Your app is now live on Vercel!
