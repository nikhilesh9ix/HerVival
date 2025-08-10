from typing import Dict, Optional, Tuple
import re
import random

class ConversationHandler:
    def __init__(self):
        # Emergency keywords with more nuanced detection
        self.emergency_keywords = {
            'suicide': [
                'kill myself', 'want to die', 'end it all', 'suicide', 'better off dead',
                'no point living', 'cant go on', "don't want to be here", 'give up on life'
            ],
            'abuse': [
                'touched', 'molested', 'raped', 'assaulted', 'abused', 'hit me', 'beats me',
                'forced me', 'inappropriate touch', 'wrong places', 'violated'
            ],
            'self_harm': [
                'cut myself', 'hurt myself', 'self harm', 'cutting', 'burn myself',
                'punish myself', 'cause pain', 'self injury', 'self mutilation'
            ],
            'harassment': [
                'stalking', 'following me', 'harassed', 'bullied', 'threatened',
                'intimidated', 'afraid of them', 'wont leave me alone', 'keeps messaging'
            ]
        }
        
        # Professional resources with more context
        self.resources = {
            'suicide': [
                {
                    'name': "National Suicide Prevention Lifeline",
                    'contact': "988",
                    'description': "24/7 support from caring professionals who understand what you're going through",
                    'available': "Available anytime, day or night"
                },
                {
                    'name': "Crisis Text Line",
                    'contact': "Text HOME to 741741",
                    'description': "Text with a trained crisis counselor in a way that might feel more comfortable",
                    'available': "24/7 text support"
                }
            ],
            'abuse': [
                {
                    'name': "RAINN National Sexual Assault Hotline",
                    'contact': "800.656.HOPE (4673)",
                    'description': "Confidential support from trained staff who understand trauma and healing",
                    'available': "24/7 confidential support"
                },
                {
                    'name': "RAINN Online Chat",
                    'contact': "https://hotline.rainn.org/online",
                    'description': "Chat online with trained support specialists in a safe, confidential environment",
                    'available': "Available 24/7"
                }
            ],
            'harassment': [
                {
                    'name': "National Center for Victims of Crime",
                    'contact': "1-855-4-VICTIM",
                    'description': "Support and advocacy for those experiencing harassment or stalking",
                    'available': "Weekdays 8:30am-8:30pm EST"
                }
            ]
        }

        # Empathetic conversation starters
        self.conversation_starters = {
            'distressed': [
                "Would you like to tell me more about what's been happening?",
                "I'm here to listen without any judgment. What's on your mind?",
                "Sometimes talking about it can help. What feels heaviest right now?",
                "Take your time - there's no rush. What would feel most helpful to share?"
            ],
            'anxious': [
                "What's making you feel most anxious right now?",
                "Would you like to explore what's causing these feelings?",
                "Sometimes anxiety can feel overwhelming. What's going through your mind?",
                "We can take this one small step at a time. What feels most pressing?"
            ],
            'lonely': [
                "It sounds like you're feeling really isolated. What's been making you feel this way?",
                "Those feelings of loneliness are so hard. Would you like to talk about it?",
                "I hear how difficult this is. What's been making you feel disconnected?"
            ]
        }

    def get_conversation_starter(self, emotion: str) -> str:
        """Get a contextually appropriate conversation starter."""
        starters = self.conversation_starters.get(emotion, self.conversation_starters['distressed'])
        return random.choice(starters)

    def detect_emergency(self, text: str) -> Tuple[Optional[str], Optional[list]]:
        """Detect if the message contains emergency keywords and return appropriate resources with context."""
        text = text.lower()
        for category, keywords in self.emergency_keywords.items():
            if any(keyword in text for keyword in keywords):
                return category, self.resources.get(category, [])
        return None, None

    def generate_response(self, message: str, emotion: str, confidence: float) -> Dict:
        """Generate a deeply personal, empathetic response based on user's message."""
        emergency_type, resources = self.detect_emergency(message)
        message_lower = message.lower()
        
        # Handle emergency situations with deep empathy
        if emergency_type == 'suicide':
            return {
                "response": (
                    "I hear the deep pain in your words, and I want you to know that your life has immense value, even if it doesn't feel that way right now. "
                    "These feelings are incredibly heavy to carry, and it makes sense that you're feeling overwhelmed. "
                    f"{self.get_conversation_starter('distressed')} "
                    "There are compassionate professionals who truly understand these feelings and want to help you through this moment - "
                    "they've helped many others who've felt exactly what you're feeling. Would you be open to talking with them? "
                    "You don't have to carry this weight alone."
                ),
                "resources": resources,
                "priority": "high"
            }
        elif emergency_type == 'abuse':
            return {
                "response": (
                    "I am so deeply sorry that this happened to you. What you experienced is a violation, and it is not your fault - not in any way. "
                    "Your feelings, whatever they may be, are completely valid. You've shown incredible courage in sharing this. "
                    f"{self.get_conversation_starter('distressed')} "
                    "There are caring professionals who specialize in supporting survivors like you - they can offer the kind of support and guidance "
                    "that could be really helpful when you're ready. Everything would be completely confidential, and you'd be in control every step of the way. "
                    "Would you like to know more about these resources?"
                ),
                "resources": resources,
                "priority": "high"
            }
        elif emergency_type == 'harassment':
            return {
                "response": (
                    "I'm so sorry you're experiencing this harassment - it's completely unfair and not at all okay. Your feelings of distress are absolutely valid. "
                    "No one deserves to feel unsafe or threatened. "
                    f"{self.get_conversation_starter('anxious')} "
                    "There are organizations that specialize in helping people in similar situations - they can help protect your rights "
                    "and work with you to create a safety plan. Would you like to know more about the support available?"
                ),
                "resources": resources,
                "priority": "high"
            }
        
        # Handle emotional states with personalized responses
        if any(word in message_lower for word in ['alone', 'lonely', 'no friends', 'no one understands', 'left out']):
            return {
                "response": (
                    "That feeling of being alone can be really painful. It's completely natural to want connection and understanding - we all do. "
                    "College life especially can feel isolating sometimes, even when surrounded by people. "
                    f"{self.get_conversation_starter('lonely')} "
                    "Remember that feeling this way doesn't mean there's anything wrong with you. Sometimes it takes time to find our people, "
                    "and that's okay. Would you like to explore some ways to start building those connections?"
                ),
                "priority": "medium"
            }
        elif any(word in message_lower for word in ['sad', 'hurt', 'pain', 'crying', 'depressed', 'heartbroken']):
            return {
                "response": (
                    "I can hear how much pain you're in, and it makes complete sense that you're feeling this way. These emotions are so intense, "
                    "and sometimes they can feel like they're taking over. "
                    f"{self.get_conversation_starter('distressed')} "
                    "You don't have to push these feelings away or try to be strong all the time. It's okay to not be okay, "
                    "and it's okay to take the time you need to process these emotions."
                ),
                "priority": "medium"
            }
        elif any(word in message_lower for word in ['scared', 'afraid', 'anxious', 'nervous', 'worry', 'panic']):
            return {
                "response": (
                    "Those anxious feelings can be really overwhelming, and I hear how much they're affecting you. Your body and mind are responding "
                    "to something that feels threatening, and that's completely valid. "
                    f"{self.get_conversation_starter('anxious')} "
                    "If you'd like, we could try a gentle grounding exercise together - something simple like focusing on your breath or noticing "
                    "things around you. What feels most helpful when anxiety is strong?"
                ),
                "priority": "medium"
            }
        elif any(word in message_lower for word in ['happy', 'better', 'good', 'hope', 'grateful', 'proud']):
            return {
                "response": (
                    "I'm really moved hearing this spark of hope in your words. These moments of light are so precious, and you're absolutely right "
                    "to acknowledge them. What you're feeling is real and valuable. Would you like to explore what's bringing you these positive "
                    "feelings? Sometimes talking about our moments of strength can help us build on them."
                ),
                "priority": "low"
            }
        else:
            return {
                "response": (
                    "Thank you for sharing with me. I want you to know that whatever you're experiencing matters, and your feelings are valid. "
                    f"{self.get_conversation_starter('distressed')} Sometimes just having someone to listen without judgment can help us process "
                    "our thoughts and feelings better."
                ),
                "priority": "low"
            }
