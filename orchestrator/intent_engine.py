"""Intent Engine v1 - Classifies user intents and routes to appropriate agents"""

from enum import Enum
from typing import Dict

# OS Configuration
OS_NAME = "Sovereign OS"
OS_VERSION = "1.5"

class IntentType(Enum):
    """Core intent classifications for the Sovereign OS"""
    BUILD = "BUILD"
    RESEARCH = "RESEARCH"
    DOCUMENT = "DOCUMENT"
    EXECUTE = "EXECUTE"
    REVIEW = "REVIEW"
    UNKNOWN = "UNKNOWN"

def classify_intent(text: str) -> Dict[str, any]:
    """
    Classify user intent using keyword matching (v1 - naive implementation)
    
    Args:
        text: User's goal or instruction
        
    Returns:
        Dict containing intent type, confidence, and routing target
    """
    text_lower = text.lower()
    
    # BUILD intent keywords
    if any(word in text_lower for word in ["build", "create", "design", "develop", "make", "construct"]):
        return {
            "intent": IntentType.BUILD.value,
            "confidence": 0.85,
            "route_to": "MindForgeArchitect"
        }
    
    # RESEARCH intent keywords
    elif any(word in text_lower for word in ["research", "analyze", "investigate", "study", "explore", "find"]):
        return {
            "intent": IntentType.RESEARCH.value,
            "confidence": 0.80,
            "route_to": "ResearchAgent"
        }
    
    # DOCUMENT intent keywords
    elif any(word in text_lower for word in ["document", "write", "record", "log", "note", "draft"]):
        return {
            "intent": IntentType.DOCUMENT.value,
            "confidence": 0.75,
            "route_to": "DocumentAgent"
        }
    
    # EXECUTE intent keywords
    elif any(word in text_lower for word in ["execute", "run", "perform", "do", "launch", "start"]):
        return {
            "intent": IntentType.EXECUTE.value,
            "confidence": 0.80,
            "route_to": "ExecutionEngine"
        }
    
    # REVIEW intent keywords
    elif any(word in text_lower for word in ["review", "check", "validate", "verify", "audit", "inspect"]):
        return {
            "intent": IntentType.REVIEW.value,
            "confidence": 0.75,
            "route_to": "GPTSecureReviewAgent"
        }
    
    # Default to UNKNOWN
    else:
        return {
            "intent": IntentType.UNKNOWN.value,
            "confidence": 0.0,
            "route_to": None
        }
