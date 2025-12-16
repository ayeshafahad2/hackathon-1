from typing import List, Optional
from ..models.data_models import Document, QueryContext
from ..services.openai_service import OpenAIService
from ..services.qdrant_service import QdrantService
from ..services.embedding_service import EmbeddingService
import logging

logger = logging.getLogger(__name__)


class RAGService:
    def __init__(self):
        self.openai_service = OpenAIService()
        self.qdrant_service = QdrantService()
        self.embedding_service = EmbeddingService()

        # Check if Qdrant is available
        self.qdrant_available = self.qdrant_service.client is not None

    async def query(self, query_context: QueryContext) -> str:
        """
        Process a query using RAG (Retrieval-Augmented Generation)
        """
        try:
            # If specific text is selected, use it directly as context
            if query_context.selected_text:
                context = query_context.selected_text
            else:
                context = ""

                # Only try to use vector database if it's available
                if self.qdrant_available:
                    try:
                        # Search for relevant documents in the vector database
                        query_embedding = await self.embedding_service.create_embedding(query_context.query)
                        relevant_docs = await self.qdrant_service.search_similar(
                            query_embedding,
                            limit=5
                        )

                        # Combine the content of relevant documents as context
                        context_parts = []
                        for doc in relevant_docs:
                            context_parts.append(doc.content)

                        context = "\n\n".join(context_parts) if context_parts else ""
                    except Exception as qdrant_error:
                        logger.warning(f"Qdrant search failed: {str(qdrant_error)}, falling back to general response")
                        context = ""
                else:
                    logger.info("Qdrant not available, using general response")

            # Generate response using OpenAI with the retrieved context (or empty if unavailable)
            response = await self.openai_service.generate_response(
                prompt=query_context.query,
                context=context,
                selected_text=query_context.selected_text
            )

            return response

        except Exception as e:
            logger.error(f"Error in RAG query processing: {str(e)}")
            # Return a helpful message instead of raising an exception
            return f"I apologize, but I encountered an error processing your request: {str(e)}. Please check that all required services are properly configured."

    async def add_document(self, document: Document) -> bool:
        """
        Add a document to the vector database for future retrieval
        """
        if not self.qdrant_available:
            logger.warning("Qdrant not available, skipping document storage")
            return False

        try:
            # Create embedding for the document if not already provided
            if not document.embedding:
                document.embedding = await self.embedding_service.create_embedding(
                    document.content
                )

            # Store the document in Qdrant
            return await self.qdrant_service.store_documents([document])

        except Exception as e:
            logger.error(f"Error adding document to RAG system: {str(e)}")
            return False

    async def add_documents(self, documents: List[Document]) -> bool:
        """
        Add multiple documents to the vector database
        """
        if not self.qdrant_available:
            logger.warning("Qdrant not available, skipping document storage")
            return False

        try:
            # Create embeddings for documents that don't have them
            for doc in documents:
                if not doc.embedding:
                    doc.embedding = await self.embedding_service.create_embedding(
                        doc.content
                    )

            # Store all documents in Qdrant
            return await self.qdrant_service.store_documents(documents)

        except Exception as e:
            logger.error(f"Error adding documents to RAG system: {str(e)}")
            return False