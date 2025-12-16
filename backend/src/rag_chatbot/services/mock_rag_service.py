from typing import List, Optional
from ..models.data_models import Document, QueryContext
from .openai_service import OpenAIService
from .mock_qdrant_service import MockQdrantService  # Using mock instead of real Qdrant
from .embedding_service import EmbeddingService


class MockRAGService:
    def __init__(self):
        self.openai_service = OpenAIService()
        self.qdrant_service = MockQdrantService()  # Using mock
        self.embedding_service = EmbeddingService()

    async def query(self, query_context: QueryContext) -> str:
        """
        Process a query using mocked RAG (Retrieval-Augmented Generation)
        """
        try:
            # If specific text is selected, use it directly as context
            if query_context.selected_text:
                context = query_context.selected_text
            else:
                # For demo, we'll just use a simple approach without real vector search
                # In production, this would search the vector database
                context = f"This is the textbook content related to your query: '{query_context.query}'. In a full implementation, this would come from the vector database based on semantic similarity."

            # Generate response using OpenAI with the retrieved context
            response = await self.openai_service.generate_response(
                prompt=query_context.query,
                context=context,
                selected_text=query_context.selected_text
            )

            return response

        except Exception as e:
            raise Exception(f"Error in RAG query processing: {str(e)}")

    async def add_document(self, document: Document) -> bool:
        """
        Add a document to the mock vector database for future retrieval
        """
        try:
            # Create embedding for the document if not already provided
            if not document.embedding:
                document.embedding = await self.embedding_service.create_embedding(
                    document.content
                )

            # Store the document in mock Qdrant
            return await self.qdrant_service.store_documents([document])

        except Exception as e:
            raise Exception(f"Error adding document to RAG system: {str(e)}")

    async def add_documents(self, documents: List[Document]) -> bool:
        """
        Add multiple documents to the mock vector database
        """
        try:
            # Create embeddings for documents that don't have them
            for doc in documents:
                if not doc.embedding:
                    doc.embedding = await self.embedding_service.create_embedding(
                        doc.content
                    )

            # Store all documents in mock Qdrant
            return await self.qdrant_service.store_documents(documents)

        except Exception as e:
            raise Exception(f"Error adding documents to RAG system: {str(e)}")