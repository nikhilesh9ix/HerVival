from typing import Dict, List, Tuple
import re

class CrisisDetector:
    def __init__(self):
        # Crisis keywords and their severity levels (1-5, 5 being most severe)
        self.crisis_patterns = {
            r"\b(kill|hurt|harm)\s*(my)?self\b": 5,
            r"\b(suicide|suicidal|end it all)\b": 5,
            r"\b(want to|wanna)\s*(die|disappear)\b": 5,
            r"\b(feel|feeling)\s*(unsafe|threatened|scared)\b": 4,
            r"\b(being|am|getting)\s*(stalked|followed|watched)\b": 4,
            r"\b(domestic|physical|sexual)\s*(violence|abuse|assault)\b": 4,
            r"\b(hopeless|worthless|helpless)\b": 3,
            r"\b(cant|cannot|can't)\s*(take|handle|cope)\s*(it|this)\b": 3,
            r"\b(nobody|no\s*one)\s*(cares|loves|helps)\b": 3,
        }

    def detect_crisis(self, text: str) -> Tuple[bool, int, List[str]]:
        """
        Analyzes text for crisis indicators.
        Returns: (is_crisis, severity_level, matched_patterns)
        """
        is_crisis = False
        max_severity = 0
        matched_patterns = []

        for pattern, severity in self.crisis_patterns.items():
            if re.search(pattern, text.lower()):
                is_crisis = True
                max_severity = max(max_severity, severity)
                matched_patterns.append(pattern)

        return is_crisis, max_severity, matched_patterns

class ResourceProvider:
    def __init__(self):
        self.emergency_resources = {
            "immediate_danger": [
                "If you're in immediate danger, please call emergency services (911 in the US)",
                "National Emergency Number: 112 (India)"
            ],
            "crisis_helplines": [
                "National Crisis Helpline (24/7): 1-800-273-8255",
                "Crisis Text Line: Text HOME to 741741",
                "Women's Helpline (India): 1091"
            ],
            "domestic_violence": [
                "National Domestic Violence Hotline: 1-800-799-SAFE (7233)",
                "Women in Distress Helpline (India): 181"
            ],
            "legal_aid": [
                "National Legal Services Authority (NALSA): 1516",
                "Legal Aid Society: Find local resources at www.legal-aid.org"
            ]
        }

        self.self_care_exercises = {
            "breathing": [
                "4-7-8 Breathing: Inhale for 4 counts, hold for 7, exhale for 8",
                "Box Breathing: Inhale 4, hold 4, exhale 4, hold 4",
                "Deep Belly Breathing: Place hand on belly, breathe deeply for 5 counts"
            ],
            "grounding": [
                "5-4-3-2-1 Technique: Name 5 things you see, 4 you feel, 3 you hear, 2 you smell, 1 you taste",
                "Body Scan: Focus attention slowly from toes to head",
                "Object Focus: Hold an object and notice its texture, temperature, and weight"
            ],
            "affirmations": [
                "I am strong and resilient",
                "I deserve peace and safety",
                "My feelings are valid",
                "I am worthy of love and respect",
                "I trust in my ability to heal"
            ]
        }

    def get_emergency_resources(self, category: str = None) -> List[str]:
        if category and category in self.emergency_resources:
            return self.emergency_resources[category]
        return [resource for resources in self.emergency_resources.values() for resource in resources]

    def get_self_care_exercise(self, exercise_type: str = None) -> List[str]:
        if exercise_type and exercise_type in self.self_care_exercises:
            return self.self_care_exercises[exercise_type]
        return [exercise for exercises in self.self_care_exercises.values() for exercise in exercises]
