from qdrant_client import QdrantClient
from qdrant_client.http import models
from typing import List, Optional
from ..models.data_models import Document
from ..config import settings
import logging

logger = logging.getLogger(__name__)


class QdrantService:
    def __init__(self):
        try:
            if settings.qdrant_api_key:
                # Handle Qdrant Cloud URL format properly
                if 'cloud.qdrant.io' in settings.qdrant_url:
                    # For cloud instances, parse hostname and port properly
                    from urllib.parse import urlparse
                    parsed_url = urlparse(settings.qdrant_url)
                    hostname = parsed_url.hostname
                    port = parsed_url.port or (443 if parsed_url.scheme == 'https' else 80)

                    self.client = QdrantClient(
                        host=hostname,
                        port=port,
                        grpc_port=-1,  # Disable gRPC for cloud
                        api_key=settings.qdrant_api_key,
                        https=True,
                        check_compatibility=False  # Skip version check to avoid warnings
                    )
                else:
                    self.client = QdrantClient(
                        url=settings.qdrant_url,
                        api_key=settings.qdrant_api_key,
                        https=settings.qdrant_url.startswith('https://'),
                        check_compatibility=False  # Skip version check to avoid warnings
                    )
            else:
                self.client = QdrantClient(
                    url=settings.qdrant_url,
                    check_compatibility=False  # Skip version check to avoid warnings
                )

            # Initialize the collection for textbook content
            self.collection_name = "textbook_content"
            # Don't initialize the collection immediately, do it on demand
            self.collection_initialized = False

            # Test connection to Qdrant
            self._test_connection()

        except Exception as e:
            logger.error(f"Failed to initialize Qdrant client: {str(e)}")
            self.client = None
            self.collection_initialized = False

    def _test_connection(self):
        """
        Test the connection to Qdrant by attempting to list collections
        """
        if not self.client:
            return False

        try:
            self.client.get_collections()
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Qdrant: {str(e)}")
            return False

    def _init_collection(self):
        """
        Initialize the Qdrant collection for storing textbook content
        """
        if not self.client:
            return False

        try:
            # Check if collection exists
            self.client.get_collection(self.collection_name)
            self.collection_initialized = True
            return True
        except:
            try:
                # Create collection if it doesn't exist
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=models.VectorParams(
                        size=1536,  # OpenAI embedding size
                        distance=models.Distance.COSINE
                    )
                )
                self.collection_initialized = True
                return True
            except Exception as e:
                logger.error(f"Failed to create collection in Qdrant: {str(e)}")
                return False

    def _ensure_collection_exists(self):
        """
        Ensure the collection exists, initialize if needed
        """
        if not self.collection_initialized:
            return self._init_collection()
        return True

    async def store_documents(self, documents: List[Document]) -> bool:
        """
        Store documents in the Qdrant collection
        """
        if not self.client:
            logger.error("Qdrant client not initialized, cannot store documents")
            return False

        try:
            # Ensure collection exists before storing
            if not self._ensure_collection_exists():
                logger.error("Failed to ensure collection exists")
                return False

            points = []
            for doc in documents:
                points.append(
                    models.PointStruct(
                        id=doc.id,
                        vector=doc.embedding if doc.embedding else [],
                        payload={
                            "content": doc.content,
                            "metadata": doc.metadata
                        }
                    )
                )

            self.client.upsert(
                collection_name=self.collection_name,
                points=points
            )
            return True
        except Exception as e:
            logger.error(f"Error storing documents in Qdrant: {str(e)}")
            return False

    async def search_similar(self, query_embedding: List[float], limit: int = 5) -> List[Document]:
        """
        Search for similar documents based on the query embedding
        """
        if not self.client:
            logger.error("Qdrant client not initialized, cannot search")
            return []

        try:
            # Ensure collection exists before searching
            if not self._ensure_collection_exists():
                logger.error("Failed to ensure collection exists")
                return []

            search_results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=limit
            )

            documents = []
            for result in search_results:
                doc = Document(
                    id=result.id,
                    content=result.payload.get("content", ""),
                    metadata=result.payload.get("metadata", {}),
                    embedding=result.vector
                )
                documents.append(doc)

            return documents
        except Exception as e:
            logger.error(f"Error searching in Qdrant: {str(e)}")
            return []

    async def get_document_by_id(self, doc_id: str) -> Optional[Document]:
        """
        Retrieve a specific document by ID
        """
        if not self.client:
            logger.error("Qdrant client not initialized, cannot retrieve document")
            return None

        try:
            # Ensure collection exists before retrieving
            if not self._ensure_collection_exists():
                logger.error("Failed to ensure collection exists")
                return None

            results = self.client.retrieve(
                collection_name=self.collection_name,
                ids=[doc_id]
            )

            if results:
                result = results[0]
                return Document(
                    id=result.id,
                    content=result.payload.get("content", ""),
                    metadata=result.payload.get("metadata", {}),
                    embedding=result.vector
                )
            return None
        except Exception as e:
            logger.error(f"Error retrieving document from Qdrant: {str(e)}")
            return None