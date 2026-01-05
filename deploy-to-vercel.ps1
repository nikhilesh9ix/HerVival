# Vercel Deployment Script for HerVival
# Run this script to prepare and deploy your app to Vercel

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  HerVival - Vercel Deployment" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Check if Vercel CLI is installed
Write-Host "Checking for Vercel CLI..." -ForegroundColor Yellow
$vercelInstalled = Get-Command vercel -ErrorAction SilentlyContinue

if (-not $vercelInstalled) {
    Write-Host "Vercel CLI not found. Installing..." -ForegroundColor Yellow
    npm install -g vercel
    Write-Host "Vercel CLI installed successfully!" -ForegroundColor Green
} else {
    Write-Host "Vercel CLI is already installed." -ForegroundColor Green
}

Write-Host ""
Write-Host "Preparing for deployment..." -ForegroundColor Yellow

# Backup original requirements
if (Test-Path "requirements.txt") {
    Write-Host "Backing up original requirements.txt..." -ForegroundColor Yellow
    Copy-Item "requirements.txt" "requirements.backup.txt" -Force
    Write-Host "Backup created: requirements.backup.txt" -ForegroundColor Green
}

# Use optimized requirements for deployment
if (Test-Path "requirements.vercel.txt") {
    Write-Host "Using optimized requirements for Vercel..." -ForegroundColor Yellow
    Copy-Item "requirements.vercel.txt" "requirements.txt" -Force
    Write-Host "Using optimized requirements.txt" -ForegroundColor Green
}

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  Important: Environment Variables" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Before deploying, make sure you have set the following" -ForegroundColor Yellow
Write-Host "environment variables in your Vercel dashboard:" -ForegroundColor Yellow
Write-Host ""
Write-Host "  - FLASK_SECRET_KEY" -ForegroundColor White
Write-Host "  - FIREBASE_API_KEY" -ForegroundColor White
Write-Host "  - FIREBASE_AUTH_DOMAIN" -ForegroundColor White
Write-Host "  - FIREBASE_PROJECT_ID" -ForegroundColor White
Write-Host "  - FIREBASE_STORAGE_BUCKET" -ForegroundColor White
Write-Host "  - FIREBASE_MESSAGING_SENDER_ID" -ForegroundColor White
Write-Host "  - FIREBASE_APP_ID" -ForegroundColor White
Write-Host "  - FIREBASE_MEASUREMENT_ID" -ForegroundColor White
Write-Host ""

$response = Read-Host "Have you set all environment variables in Vercel? (y/n)"

if ($response -ne "y") {
    Write-Host ""
    Write-Host "Please set up your environment variables first:" -ForegroundColor Red
    Write-Host "1. Go to https://vercel.com/dashboard" -ForegroundColor White
    Write-Host "2. Select your project (or create a new one)" -ForegroundColor White
    Write-Host "3. Go to Settings > Environment Variables" -ForegroundColor White
    Write-Host "4. Add all required variables" -ForegroundColor White
    Write-Host ""
    Write-Host "Run this script again when ready." -ForegroundColor Yellow
    
    # Restore original requirements
    if (Test-Path "requirements.backup.txt") {
        Copy-Item "requirements.backup.txt" "requirements.txt" -Force
    }
    exit
}

Write-Host ""
Write-Host "Starting deployment..." -ForegroundColor Green
Write-Host ""

# Deploy to Vercel
vercel --prod

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  Deployment Complete!" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Restore original requirements
if (Test-Path "requirements.backup.txt") {
    Write-Host "Restoring original requirements.txt..." -ForegroundColor Yellow
    Copy-Item "requirements.backup.txt" "requirements.txt" -Force
    Remove-Item "requirements.backup.txt" -Force
    Write-Host "Original requirements.txt restored." -ForegroundColor Green
}

Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Test your deployed app at the URL shown above" -ForegroundColor White
Write-Host "2. Update Firebase configuration to whitelist your Vercel domain" -ForegroundColor White
Write-Host "3. Test authentication and all features" -ForegroundColor White
Write-Host ""
Write-Host "For troubleshooting, check: https://vercel.com/docs" -ForegroundColor Cyan
