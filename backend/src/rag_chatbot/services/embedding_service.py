from typing import List
from ..config import settings
from ..services.openai_service import OpenAIService


class EmbeddingService:
    def __init__(self):
        self.openai_service = OpenAIService()

    async def create_embedding(self, text: str) -> List[float]:
        """
        Create a single embedding for the given text
        """
        embeddings = await self.openai_service.create_embeddings([text])
        return embeddings[0] if embeddings else []

    async def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Create embeddings for multiple texts
        """
        return await self.openai_service.create_embeddings(texts)

    async def calculate_similarity(self, text1: str, text2: str) -> float:
        """
        Calculate cosine similarity between two texts based on their embeddings
        """
        emb1 = await self.create_embedding(text1)
        emb2 = await self.create_embedding(text2)

        if not emb1 or not emb2 or len(emb1) != len(emb2):
            return 0.0

        # Calculate cosine similarity
        dot_product = sum(a * b for a, b in zip(emb1, emb2))
        magnitude1 = sum(a * a for a in emb1) ** 0.5
        magnitude2 = sum(b * b for b in emb2) ** 0.5

        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0

        return dot_product / (magnitude1 * magnitude2)