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
Write-Host "2. Test chat and all features" -ForegroundColor White
Write-Host "3. Note: Authentication has been removed - all pages are now public" -ForegroundColor White
Write-Host ""
Write-Host "For troubleshooting, check: https://vercel.com/docs" -ForegroundColor Cyan
