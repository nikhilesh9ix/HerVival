from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import logging
import os
from conversation_handler import ConversationHandler
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Initialize conversation handler
conversation_handler = ConversationHandler()

@app.route('/')
def index():
    """Render the main chat interface."""
    return render_template('index.html')

@app.route('/counselors')
def counselors():
    """Render the counselors page."""
    return render_template('counselors.html')

@app.route('/services')
def services():
    """Render the emergency services page."""
    return render_template('services.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages with emotion-aware responses."""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({
                "response": "I notice you haven't shared anything yet. Would you like to tell me what's on your mind?",
                "priority": "low"
            })
        
        # Generate empathetic response
        response_data = conversation_handler.generate_response(
            message=user_message,
            emotion=data.get('emotion', 'neutral'),
            confidence=data.get('confidence', 0.8)
        )
        
        return jsonify(response_data)
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({
            "response": (
                "I'm having a moment of difficulty processing your message, but I want you to know that your "
                "feelings and needs matter. Could you try sharing that with me again? If you need immediate "
                "support, I can provide you with contact information for professional help."
            ),
            "priority": "medium",
            "error": str(e)
        }), 500

@app.route('/user/activity', methods=['POST'])
def update_activity():
    """Update user's last active timestamp."""
    return jsonify({'status': 'success'})

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors with empathetic message."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors with supportive message."""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({
        "response": (
            "I'm experiencing some technical difficulties, but I want to make sure you get the support "
            "you need. If you need immediate assistance, please don't hesitate to reach out to our "
            "emergency support services."
        ),
        "priority": "high"
    }), 500

# For Vercel deployment
application = app

if __name__ == '__main__':
    logger.info("Starting HerVival support system...")
    app.run(debug=True, port=5001)
