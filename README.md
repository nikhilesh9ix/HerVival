# HerVival 🌸

> **Empowering women through AI-powered emotional support and crisis intervention**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com/nikhilesh9ix/HerVival)

---

## 🌟 Overview

**HerVival** is an intelligent emotional support platform designed specifically to help women navigate emotional challenges, detect crisis situations, and access critical mental health resources. Using advanced natural language processing and pattern recognition, HerVival provides empathetic, context-aware responses while ensuring safety through real-time crisis detection.

### 🎯 Mission

To create a safe, accessible, and judgment-free space where women can seek emotional support, receive immediate crisis intervention, and connect with professional resources when needed.

### ✨ Why HerVival?

- **Privacy-First**: Your conversations remain confidential
- **24/7 Availability**: Support whenever you need it
- **Crisis-Aware**: Intelligent detection and immediate resource provision
- **Culturally Sensitive**: Resources tailored for diverse communities
- **No Judgment**: A safe space to express your feelings

---

## 🚀 Features

### 🧠 **Emotion-Aware Conversations**
- Advanced emotion detection and analysis
- Context-aware, empathetic responses
- Personalized support based on emotional state
- Natural conversation flow

### 🚨 **Multi-Level Crisis Detection**
- **Level 5 (Critical)**: Suicide ideation, immediate self-harm
- **Level 4 (High)**: Abuse, stalking, safety threats
- **Level 3 (Medium)**: Severe emotional distress, hopelessness
- Automatic escalation to emergency resources
- Pattern-matching for crisis keywords

### 💬 **Interactive Chat Interface**
- Clean, intuitive design
- Real-time message processing
- Mobile-responsive layout
- Accessibility-friendly

### 🏥 **Comprehensive Resource Directory**
- **Emergency Hotlines**: 24/7 crisis support
- **Professional Counselors**: Licensed therapists and counselors
- **Support Groups**: Community resources
- **Legal Aid**: Domestic violence and harassment support

### 🔒 **Privacy & Security**
- Secure session management
- Environment-based configuration
- No conversation storage
- CORS-enabled for cross-origin security

---

## 🎬 Demo

### Live Application
🌐 **Deployed URL**: [https://her-vival.vercel.app/](https://her-vival.vercel.app/)

### Screenshots

```
┌─────────────────────────────────────┐
│  🌸 HerVival - Chat Interface       │
├─────────────────────────────────────┤
│                                     │
│  User: I'm feeling overwhelmed...   │
│                                     │
│  HerVival: I hear you, and your    │
│  feelings are valid. Let's talk     │
│  about what's going on...           │
│                                     │
└─────────────────────────────────────┘
```

---

## 🛠️ Technology Stack

### **Backend**
- **Flask** 3.0.0 - Web framework
- **Python** 3.8+ - Core language
- **Flask-CORS** 5.0.1 - Cross-origin resource sharing

### **Frontend**
- **HTML5** - Structure
- **CSS3** - Styling & animations
- **JavaScript** (Vanilla) - Interactivity

### **Development Tools**
- **python-dotenv** 1.0.0 - Environment management
- **requests** 2.31.0 - HTTP library

### **Deployment**
- **Vercel** - Serverless deployment
- **Git** - Version control

---

## 📦 Installation

### Prerequisites

- **Python**: 3.8 or higher
- **pip**: Latest version
- **Git**: For cloning the repository

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/nikhilesh9ix/HerVival.git
cd HerVival

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create .env file (see Configuration section)
cp .env.example .env

# 6. Run the application
python app.py
```

The application will be available at **http://localhost:5001**

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Flask Configuration
FLASK_SECRET_KEY=your-secure-random-secret-key-here
FLASK_ENV=development  # Use 'production' for deployment

# Firebase Configuration (Optional)
FIREBASE_API_KEY=your-firebase-api-key
FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_STORAGE_BUCKET=your-project.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID=your-sender-id
FIREBASE_APP_ID=your-app-id
FIREBASE_MEASUREMENT_ID=your-measurement-id
```

### Generating Secure Keys

```python
# Generate Flask secret key
import secrets
print(secrets.token_hex(32))
```

### Port Configuration

Default port: **5001**  
To change, modify in [app.py](app.py):
```python
app.run(debug=True, port=YOUR_PORT)
```

---

## 💡 Usage

### Starting a Conversation

1. **Navigate to Home**: Open http://localhost:5001
2. **Start Chatting**: Type your message in the input field
3. **Receive Support**: Get empathetic, context-aware responses
4. **Access Resources**: View counselors and emergency services pages

### Example Interactions

**Emotional Support:**
```
User: I'm feeling really anxious about my exams
HerVival: It's completely normal to feel anxious about exams. Your feelings are valid...
```

**Crisis Detection:**
```
User: [Crisis-related message]
HerVival: I'm very concerned about what you've shared. Please know that help is available.
         Here are immediate resources: [Emergency contacts displayed]
```

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main chat interface |
| `/chat` | POST | Process chat messages |
| `/counselors` | GET | Professional resources page |
| `/services` | GET | Emergency services page |
| `/user/activity` | POST | Update user activity |

---

## 📁 Project Structure

```
HerVival/
│
├── app.py                      # Flask application & routes
├── conversation_handler.py     # Conversation logic & emotion handling
├── crisis_support.py          # Crisis detection algorithms
├── requirements.txt           # Python dependencies
├── requirements.vercel.txt    # Vercel-specific dependencies
├── vercel.json               # Vercel deployment configuration
├── .env                      # Environment variables (create this)
├── .gitignore               # Git ignore rules
│
├── static/                   # Static assets
│   └── images/              # Image files
│       └── jpg2png/         # Converted images
│
├── templates/               # HTML templates
│   ├── index.html          # Main chat interface
│   ├── auth.html           # Authentication page
│   ├── counselors.html     # Counselor directory
│   ├── services.html       # Emergency services
│   └── 404.html           # Error page
│
├── deploy-to-vercel.ps1    # Deployment script
├── QUICK_DEPLOY.md         # Quick deployment guide
├── VERCEL_DEPLOYMENT.md    # Detailed deployment docs
└── README.md              # This file
```

---

## 📚 API Documentation

### POST /chat

Process user messages and generate empathetic responses.

**Request Body:**
```json
{
  "message": "User message text",
  "emotion": "neutral|happy|sad|anxious|angry",
  "confidence": 0.8
}
```

**Response:**
```json
{
  "response": "AI-generated response",
  "priority": "low|medium|high|critical",
  "resources": [...],  // If crisis detected
  "severity": 0-5      // Crisis severity level
}
```

**Status Codes:**
- `200` - Success
- `500` - Internal server error

---

##  Security

### Best Practices Implemented

✅ **Environment Variables**: All secrets in `.env` (not committed)  
✅ **CORS Protection**: Controlled cross-origin requests  
✅ **Input Validation**: Server-side message validation  
✅ **Error Handling**: Graceful error responses without exposing internals  
✅ **Session Security**: Secure session management  

### Security Checklist

- [ ] Never commit `.env` file
- [ ] Use strong, random secret keys
- [ ] Enable HTTPS in production
- [ ] Regularly update dependencies
- [ ] Monitor for security vulnerabilities
- [ ] Implement rate limiting (future)

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Contribution Guidelines

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit** your changes
   ```bash
   git commit -m "Add amazing feature"
   ```
4. **Push** to your branch
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open** a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests (when available)
pytest tests/

# Check code style
flake8 app.py conversation_handler.py crisis_support.py
```

### Areas for Contribution

- 🌐 Multi-language support
- 🧪 Unit and integration tests
- 📱 Mobile app development
- 🎨 UI/UX improvements
- 📊 Analytics and insights
- 🔒 Enhanced security features

---

##  License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 Nikhilesh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 🆘 Support & Resources

### Emergency Resources

🇺🇸 **United States**
- National Suicide Prevention Lifeline: **988**
- Crisis Text Line: Text **HOME** to **741741**
- RAINN Sexual Assault Hotline: **1-800-656-4673**
- National Domestic Violence Hotline: **1-800-799-7233**

🇮🇳 **India**
- Women Helpline: **1091**
- National Emergency Number: **112**
- Mental Health Helpline: **9152987821**
- Women in Distress: **181**

### Project Support

- 📧 **Email**: [your-email@example.com]
- 🐛 **Issues**: [GitHub Issues](https://github.com/nikhilesh9ix/HerVival/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/nikhilesh9ix/HerVival/discussions)

### Acknowledgments

This project was developed as part of a BTech academic initiative to address mental health challenges faced by women through technology.

**Special Thanks:**
- Open-source community
- Mental health professionals who provided guidance
- Beta testers and early users

---

## ⚠️ Important Disclaimers

> **Medical Disclaimer**: HerVival is an emotional support tool and **NOT** a replacement for professional mental health services, emergency services, or medical treatment. If you are experiencing a medical or mental health emergency, please contact emergency services immediately.

> **Privacy Notice**: While we prioritize privacy, please avoid sharing sensitive personal information such as exact locations, full names, or financial details in the chat.

> **Crisis Warning**: If you are in immediate danger, please call your local emergency number (911 in US, 112 in India) or go to the nearest emergency room.

---

## 💖 Final Note

Your mental health matters. Your feelings are valid. You are not alone.

If you're struggling, please reach out to professional resources. This tool is here to support you, but human connection and professional care are irreplaceable.

**Stay strong. Stay connected. Survive and thrive. 🌸**

---

<div align="center">

Made with 💙 by [Nikhilesh](https://github.com/nikhilesh9ix)

⭐ Star this repo if it helped you!

[Report Bug](https://github.com/nikhilesh9ix/HerVival/issues) • [Request Feature](https://github.com/nikhilesh9ix/HerVival/issues) • [Documentation](https://github.com/nikhilesh9ix/HerVival/wiki)

</div>
