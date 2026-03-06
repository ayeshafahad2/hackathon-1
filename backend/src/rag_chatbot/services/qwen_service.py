"""
Qwen LLM Service for RAG Chatbot
Integration with Alibaba Cloud's Qwen API
"""

import os
import logging
from typing import List, Dict, Any, Optional
import httpx

logger = logging.getLogger(__name__)

class QwenService:
    """Service for interacting with Qwen LLM API"""
    
    def __init__(self):
        """Initialize Qwen service"""
        self.api_key = os.getenv("QWEN_API_KEY", "")
        self.api_url = os.getenv("QWEN_API_URL", "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation")
        self.model = os.getenv("QWEN_MODEL", "qwen-turbo")
        self.enabled = bool(self.api_key)
        
        if not self.enabled:
            logger.warning("Qwen API key not configured. Using mock responses.")
    
    async def generate_response(
        self,
        system_prompt: str,
        user_prompt: str,
        chat_history: Optional[List[Dict[str, str]]] = None
    ) -> Dict[str, Any]:
        """
        Generate response using Qwen API
        
        Args:
            system_prompt: System instructions
            user_prompt: User's question
            chat_history: Optional conversation history
            
        Returns:
            Dictionary with response text and metadata
        """
        if not self.enabled:
            return self._generate_mock_response(user_prompt)
        
        try:
            # Build messages
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            
            # Add chat history if provided
            if chat_history:
                messages = messages[:1] + chat_history + [messages[1]]
            
            # Prepare request
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": self.model,
                "input": {
                    "messages": messages
                },
                "parameters": {
                    "temperature": 0.7,
                    "max_tokens": 1024,
                    "top_p": 0.9,
                    "repetition_penalty": 1.1
                }
            }
            
            # Make API request
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    self.api_url,
                    headers=headers,
                    json=payload
                )
                
                if response.status_code == 200:
                    result = response.json()
                    return {
                        "response": result["output"]["text"],
                        "model": self.model,
                        "usage": result.get("usage", {}),
                        "finish_reason": result["output"].get("finish_reason", "stop")
                    }
                else:
                    logger.error(f"Qwen API error: {response.status_code} - {response.text}")
                    return self._generate_mock_response(user_prompt, error=True)
                    
        except Exception as e:
            logger.error(f"Error calling Qwen API: {e}")
            return self._generate_mock_response(user_prompt, error=True)
    
    def _generate_mock_response(self, user_prompt: str, error: bool = False) -> Dict[str, Any]:
        """Generate a mock response when API is not available"""
        if error:
            text = "I'm experiencing technical difficulties right now. Please try again in a moment."
        else:
            text = "This is a mock response. To get real AI responses, please configure the Qwen API key in your environment variables."
        
        return {
            "response": text,
            "model": "mock",
            "usage": {"input_tokens": 0, "output_tokens": 0},
            "finish_reason": "mock"
        }
    
    def is_available(self) -> bool:
        """Check if Qwen API is available"""
        return self.enabled


# Global Qwen service instance
_qwen_service = None

def get_qwen_service() -> QwenService:
    """Get or create the global Qwen service instance"""
    global _qwen_service
    if _qwen_service is None:
        _qwen_service = QwenService()
    return _qwen_service
