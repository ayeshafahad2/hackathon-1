"""
Vector Store Service for RAG Chatbot
Uses ChromaDB for efficient similarity search
"""

import chromadb
from chromadb.config import Settings
from typing import List, Dict, Any, Optional
import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)

class VectorStoreService:
    """Service for managing vector database operations"""
    
    def __init__(self, persist_directory: str = "./chroma_db"):
        """
        Initialize the vector store service
        
        Args:
            persist_directory: Directory to persist ChromaDB data
        """
        self.persist_directory = persist_directory
        self.client = None
        self.collection = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize ChromaDB client and collection"""
        try:
            # Create persist directory if it doesn't exist
            Path(self.persist_directory).mkdir(parents=True, exist_ok=True)
            
            # Initialize persistent client
            logger.info(f"Initializing ChromaDB with persist directory: {self.persist_directory}")
            self.client = chromadb.PersistentClient(
                path=self.persist_directory,
                settings=Settings(
                    anonymized_telemetry=False,
                    allow_reset=True
                )
            )
            
            # Get or create collection
            self.collection = self.client.get_or_create_collection(
                name="textbook_content",
                metadata={"description": "Physical AI & Humanoid Robotics textbook content", "hnsw:space": "cosine"}
            )
            
            logger.info("ChromaDB initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize ChromaDB: {e}")
            raise
    
    def add_documents(
        self,
        documents: List[str],
        embeddings: List[List[float]],
        metadatas: List[Dict[str, Any]],
        ids: Optional[List[str]] = None
    ):
        """
        Add documents to the vector store
        
        Args:
            documents: List of text documents
            embeddings: List of embedding vectors
            metadatas: List of metadata dictionaries
            ids: Optional list of document IDs (auto-generated if not provided)
        """
        if not documents:
            logger.warning("No documents to add")
            return
        
        if ids is None:
            ids = [f"doc_{i}" for i in range(len(documents))]
        
        try:
            # ChromaDB requires specific types
            self.collection.add(
                documents=documents,
                embeddings=[emb.tolist() if hasattr(emb, 'tolist') else list(emb) for emb in embeddings],
                metadatas=metadatas,
                ids=ids
            )
            logger.info(f"Added {len(documents)} documents to vector store")
        except Exception as e:
            logger.error(f"Error adding documents: {e}")
            raise
    
    def search(
        self,
        query_embedding: List[float],
        n_results: int = 5,
        filter_metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Search for similar documents
        
        Args:
            query_embedding: Query embedding vector
            n_results: Number of results to return
            filter_metadata: Optional metadata filter
            
        Returns:
            Dictionary with documents, metadatas, distances, etc.
        """
        try:
            results = self.collection.query(
                query_embeddings=[query_embedding.tolist() if hasattr(query_embedding, 'tolist') else list(query_embedding)],
                n_results=n_results,
                where=filter_metadata,
                include=["documents", "metadatas", "distances"]
            )
            
            # Format results
            formatted_results = {
                "documents": results["documents"][0] if results["documents"] else [],
                "metadatas": results["metadatas"][0] if results["metadatas"] else [],
                "distances": results["distances"][0] if results["distances"] else []
            }
            
            return formatted_results
        except Exception as e:
            logger.error(f"Error searching documents: {e}")
            raise
    
    def get_collection_stats(self) -> Dict[str, Any]:
        """Get statistics about the collection"""
        try:
            count = self.collection.count()
            return {
                "total_documents": count,
                "collection_name": self.collection.name
            }
        except Exception as e:
            logger.error(f"Error getting collection stats: {e}")
            return {"error": str(e)}
    
    def delete_all(self):
        """Delete all documents from the collection (for development)"""
        try:
            # Reset by deleting and recreating collection
            self.client.delete_collection(self.collection.name)
            self.collection = self.client.get_or_create_collection(
                name="textbook_content",
                metadata={"description": "Physical AI & Humanoid Robotics textbook content"}
            )
            logger.info("All documents deleted from vector store")
        except Exception as e:
            logger.error(f"Error deleting documents: {e}")
            raise
    
    def reset(self):
        """Reset the vector store"""
        self.delete_all()


# Global vector store instance
_vector_store = None

def get_vector_store() -> VectorStoreService:
    """Get or create the global vector store instance"""
    global _vector_store
    if _vector_store is None:
        _vector_store = VectorStoreService()
    return _vector_store
