# Vercel Deployment Guide for HerVival

## Prerequisites
- A Vercel account (sign up at https://vercel.com)
- Git repository (already set up)

## Deployment Steps

### 1. Install Vercel CLI (Optional but recommended)
```bash
npm install -g vercel
```

### 2. Deploy to Vercel

#### Option A: Deploy via Vercel Dashboard (Easiest)
1. Go to https://vercel.com/new
2. Import your GitHub repository
3. Vercel will automatically detect the `vercel.json` configuration
4. Click "Deploy"

#### Option B: Deploy via CLI
```bash
# From your project directory
cd "c:\Files\Files\BTech College\Portfolio\Projects\Hervival\HerVival"

# Login to Vercel
vercel login

# Deploy
vercel

# For production deployment
vercel --prod
```

### 3. Post-Deployment
- Your app will be available at `https://your-project-name.vercel.app`
- Test all features including chat functionality
- **Note**: Authentication has been removed, so all pages are now publicly accessible

## Important Notes

### Limitations on Vercel
1. **Function Execution Time**: Vercel serverless functions have a 10-second timeout on Hobby plan (60s on Pro)
2. **Cold Starts**: First request might be slower due to serverless function initialization
3. **No Persistent File System**: Use external storage for any file operations
4. **ML Models**: Heavy ML models in requirements.txt might cause issues. Consider:
   - Using lighter alternatives
   - Using external API services
   - Optimizing model loading

### Optimizing for Vercel

**Good News**: Your app doesn't actually use the heavy ML libraries (`transformers` and `torch`) that are listed in requirements.txt. 

**Two Options:**

1. **Option 1 (Recommended)**: Rename requirements file before deploying
   ```bash
   # Backup original
   mv requirements.txt requirements.original.txt
   
   # Use optimized version for Vercel
   mv requirements.vercel.txt requirements.txt
   
   # Deploy
   vercel --prod
   
   # After deployment, restore if needed
   mv requirements.original.txt requirements.txt
   ```

2. **Option 2**: Remove unused packages from requirements.txt
   - Remove `transformers==4.36.0`
   - Remove `torch==2.2.1`
   - Remove `nltk==3.8.1`
   - Remove `numpy==1.24.3` (unless used elsewhere)

The optimized `requirements.vercel.txt` contains only the packages your app actually uses:
- flask==3.0.0
- python-dotenv==1.0.0
- flask-cors==5.0.1
- requests==2.31.0

### Troubleshooting

**Build fails due to package size:**
- Consider removing `transformers==4.36.0` and `torch==2.2.1` if not actively used
- Use Hugging Face Inference API instead

**Environment variables not loading:**
- Ensure all environment variables are set in Vercel dashboard
- Redeploy after adding variables

**404 errors:**
- Check that `vercel.json` routes are correct
- Ensure all template files are included in deployment

## Configuration Files Created

1. **vercel.json** - Vercel deployment configuration
2. **.vercelignore** - Files to exclude from deployment

## Monitoring and Logs
- View deployment logs in Vercel dashboard
- Access runtime logs under your project's "Logs" tab
- Set up integrations for error tracking (Sentry, etc.)

## Custom Domain (Optional)
1. Go to Project Settings → Domains
2. Add your custom domain
3. Follow DNS configuration instructions

## Support
For issues specific to Vercel deployment, refer to:
- Vercel Documentation: https://vercel.com/docs
- Python on Vercel: https://vercel.com/docs/functions/runtimes/python
