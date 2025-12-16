from openai import AsyncOpenAI
from typing import List, Dict, Any
from ..config import settings
from ..models.data_models import Document


class OpenAIService:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)

    async def generate_response(self, prompt: str, context: str = "", selected_text: str = None) -> str:
        """
        Generate a response using OpenAI's GPT model with the provided context
        """
        try:
            # Build the system message with context
            system_message = f"""
            You are an AI assistant for the Physical AI & Humanoid Robotics textbook.
            Answer the user's questions based on the provided context.
            If the answer cannot be found in the context, say so clearly.
            Keep responses concise and relevant to the textbook content.
            """

            # If selected text is provided, focus the response on that text
            if selected_text:
                system_message += f"\n\nThe user has selected this specific text to ask about: {selected_text}"
                user_message = f"Based on the selected text, {prompt}"
            else:
                user_message = prompt

            messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {user_message}"}
            ]

            response = await self.client.chat.completions.create(
                model=settings.openai_model,
                messages=messages,
                max_tokens=1000,
                temperature=0.7,
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            raise Exception(f"Error generating response from OpenAI: {str(e)}")

    async def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Create embeddings for the provided texts using OpenAI's embedding model
        """
        try:
            response = await self.client.embeddings.create(
                input=texts,
                model=settings.embedding_model
            )

            return [item.embedding for item in response.data]

        except Exception as e:
            raise Exception(f"Error creating embeddings: {str(e)}")