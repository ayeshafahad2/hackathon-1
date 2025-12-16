from qdrant_client import QdrantClient
from ..config import settings


class QdrantClientWrapper:
    """
    Wrapper class for Qdrant client to provide singleton pattern
    and centralized configuration
    """
    _instance = None
    _client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(QdrantClientWrapper, cls).__new__(cls)
            cls._instance._initialize_client()
        return cls._instance

    def _initialize_client(self):
        """
        Initialize the Qdrant client with settings
        """
        if settings.qdrant_api_key:
            self._client = QdrantClient(
                url=settings.qdrant_url,
                api_key=settings.qdrant_api_key,
            )
        else:
            self._client = QdrantClient(url=settings.qdrant_url)

    @property
    def client(self):
        """
        Get the Qdrant client instance
        """
        if self._client is None:
            self._initialize_client()
        return self._client

    def get_client(self):
        """
        Get the Qdrant client instance (alternative method)
        """
        return self._client


# Create a singleton instance
qdrant_client = QdrantClientWrapper()