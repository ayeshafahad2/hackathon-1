import google.generativeai as genai
from typing import List, Dict, Any
from ..config import settings
from ..models.data_models import Document
import logging

logger = logging.getLogger(__name__)


class GeminiService:
    def __init__(self):
        if not settings.gemini_api_key:
            raise ValueError("GEMINI_API_KEY not found in settings")
        
        genai.configure(api_key=settings.gemini_api_key)
        self.model = genai.GenerativeModel(settings.gemini_model or "gemini-pro")

    async def generate_response(self, prompt: str, context: str = "", selected_text: str = None) -> str:
        """
        Generate a response using Google's Gemini model with the provided context
        """
        try:
            # Build the system message with context
            system_message = f"""
            You are an AI assistant for the Physical AI & Humanoid Robotics textbook.
            Answer the user's questions based on the provided context.
            If the answer cannot be found in the context, say so clearly.
            Keep responses concise and relevant to the textbook content.
            Be professional and courteous - welcome users when they first interact,
            and thank them when they say goodbye.
            """

            # Handle greetings and farewells
            prompt_lower = prompt.lower()
            if any(greeting in prompt_lower for greeting in ["hello", "hi", "hey", "good morning", "good afternoon"]):
                return "Hello! Welcome to the Physical AI & Humanoid Robotics textbook assistant. I'm here to help you understand concepts related to Physical AI and Humanoid Robotics. How can I assist you today?"
            elif any(farewell in prompt_lower for farewell in ["bye", "goodbye", "see you", "exit", "quit"]):
                return "Thank you for visiting the Physical AI & Humanoid Robotics textbook assistant. Feel free to come back anytime with more questions. Have a great day!"
            
            # If selected text is provided, focus the response on that text
            if selected_text:
                system_message += f"\n\nThe user has selected this specific text to ask about: {selected_text}"
                user_message = f"Based on the selected text, {prompt}"
            else:
                user_message = prompt

            # Combine context and user message
            full_prompt = f"Context: {context}\n\nQuestion: {user_message}"

            response = await self.model.generate_content_async(full_prompt)
            
            return response.text.strip()

        except Exception as e:
            logger.error(f"Error generating response from Gemini: {str(e)}")
            return f"I apologize, but I encountered an error processing your request: {str(e)}. Please try again."

    async def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Create embeddings for the provided texts using Google's embedding model
        """
        try:
            import google.generativeai as genai
            
            embeddings = []
            for text in texts:
                result = await genai.embed_content_async(
                    model="embedding-001",
                    content=text,
                    task_type="retrieval_document"
                )
                embeddings.append(result['embedding'])
            
            return embeddings

        except Exception as e:
            logger.error(f"Error creating embeddings: {str(e)}")
            raise Exception(f"Error creating embeddings: {str(e)}")