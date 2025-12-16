from typing import List, Optional
from ..models.data_models import Document


class MockQdrantService:
    def __init__(self):
        # Mock collection to store documents in memory for testing
        self.documents = {}
        self.collection_name = "textbook_content"

    def _init_collection(self):
        # For mock service, just initialize internal data structure
        self.documents = {}
        print(f"Mock collection '{self.collection_name}' initialized")

    async def store_documents(self, documents: List[Document]) -> bool:
        """
        Store documents in the mock collection
        """
        try:
            for doc in documents:
                self.documents[doc.id] = {
                    "content": doc.content,
                    "metadata": doc.metadata,
                    "embedding": doc.embedding
                }
            print(f"Stored {len(documents)} documents in mock collection")
            return True
        except Exception as e:
            print(f"Error storing documents in mock Qdrant: {str(e)}")
            return False

    async def search_similar(self, query_embedding: List[float], limit: int = 5) -> List[Document]:
        """
        Mock search that returns some sample documents
        In a real implementation, this would perform vector similarity search
        """
        try:
            # For demo purposes, return some mock documents
            mock_docs = []
            for i in range(min(limit, 3)):  # Return max 3 mock documents
                mock_doc = Document(
                    id=f"mock_doc_{i}",
                    content=f"This is mock content related to your query. This demonstrates RAG functionality (Document {i}).",
                    metadata={"source": "mock", "relevance": 0.9}
                )
                mock_docs.append(mock_doc)
            return mock_docs
        except Exception as e:
            print(f"Error searching in mock Qdrant: {str(e)}")
            return []

    async def get_document_by_id(self, doc_id: str) -> Optional[Document]:
        """
        Retrieve a specific document by ID from mock storage
        """
        try:
            if doc_id in self.documents:
                doc_data = self.documents[doc_id]
                return Document(
                    id=doc_id,
                    content=doc_data["content"],
                    metadata=doc_data["metadata"],
                    embedding=doc_data["embedding"]
                )
            return None
        except Exception as e:
            print(f"Error retrieving document from mock Qdrant: {str(e)}")
            return None