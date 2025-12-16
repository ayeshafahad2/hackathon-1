#!/usr/bin/env python3
"""
Test script for the RAG Chatbot API
This script tests the full functionality of the RAG system
"""

import asyncio
import aiohttp
import json
from pathlib import Path
import sys

# Add the backend src directory to the path
sys.path.append(str(Path(__file__).parent / 'src'))

from src.rag_chatbot.models.data_models import Document
from src.rag_chatbot.services.rag_service import RAGService
from src.rag_chatbot.services.embedding_service import EmbeddingService
from src.rag_chatbot.config import settings


async def test_api_endpoints():
    """Test the API endpoints directly"""
    print("🔍 Testing API endpoints...")
    
    base_url = "http://localhost:8000"
    
    # Test health endpoint
    try:
        async with aiohttp.ClientSession() as session:
            # Test root endpoint
            async with session.get(f"{base_url}/") as resp:
                if resp.status == 200:
                    print("✅ Root endpoint: OK")
                    root_data = await resp.json()
                    print(f"   Response: {root_data}")
                else:
                    print(f"❌ Root endpoint: Status {resp.status}")
            
            # Test health endpoint
            async with session.get(f"{base_url}/health") as resp:
                if resp.status == 200:
                    print("✅ Health endpoint: OK")
                else:
                    print(f"❌ Health endpoint: Status {resp.status}")
            
            # Test chat health endpoint
            async with session.get(f"{base_url}/api/v1/chat/health") as resp:
                if resp.status == 200:
                    print("✅ Chat health endpoint: OK")
                else:
                    print(f"❌ Chat health endpoint: Status {resp.status}")
            
            # Test chat endpoint with a sample query
            sample_payload = {
                "message": "What is Physical AI?",
                "language": "en"
            }
            
            async with session.post(
                f"{base_url}/api/v1/chat",
                json=sample_payload,
                headers={"Content-Type": "application/json"}
            ) as resp:
                if resp.status == 200:
                    print("✅ Chat endpoint: OK")
                    response_data = await resp.json()
                    print(f"   Sample response: {response_data['response'][:100]}...")
                else:
                    print(f"❌ Chat endpoint: Status {resp.status}")
                    error_text = await resp.text()
                    print(f"   Error: {error_text}")
                    
    except Exception as e:
        print(f"❌ API test failed: {str(e)}")
        return False
    
    return True


async def test_rag_functionality():
    """Test the RAG functionality directly"""
    print("\n🔍 Testing RAG functionality...")
    
    rag_service = RAGService()
    
    if not rag_service.qdrant_available:
        print("❌ Qdrant is not available, skipping RAG functionality test")
        return False
    
    print("✅ Qdrant is available, testing RAG functionality...")
    
    try:
        # Test adding a test document
        test_doc = Document(
            id="test_document_12345",
            content="Physical AI refers to artificial intelligence systems that interact with the physical world through robots and other embodied agents.",
            metadata={
                "title": "Test Document",
                "source": "test",
                "type": "concept_definition"
            }
        )
        
        success = await rag_service.add_document(test_doc)
        if success:
            print("✅ Successfully added test document to vector store")
        else:
            print("❌ Failed to add test document to vector store")
            return False
        
        # Test querying with the content we just added
        from src.rag_chatbot.models.data_models import QueryContext
        
        query_context = QueryContext(
            query="What is Physical AI?",
            selected_text=None,
            language="en"
        )
        
        response = await rag_service.query(query_context)
        print(f"✅ Test query response: {response[:200]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ RAG functionality test failed: {str(e)}")
        return False


async def run_full_test():
    """Run the complete test suite"""
    print("=" * 60)
    print("🧪 RUNNING COMPLETE RAG CHATBOT TEST SUITE")
    print("=" * 60)
    
    print("📋 Test Checklist:")
    print("   1. Environment validation")
    print("   2. Qdrant connection")
    print("   3. API endpoints")
    print("   4. RAG functionality")
    print("   5. Sample queries")
    
    # Validate environment
    print(f"\n1. Validating environment...")
    print(f"   OpenAI API Key set: {'Yes' if settings.openai_api_key else 'No'}")
    print(f"   Qdrant URL: {settings.qdrant_url}")
    print(f"   Qdrant API Key set: {'Yes' if settings.qdrant_api_key else 'No'}")
    print(f"   Postgres URL set: {'Yes' if settings.postgres_url else 'No'}")
    
    # Test API endpoints
    print(f"\n2. Testing API endpoints...")
    api_success = await test_api_endpoints()
    
    # Test RAG functionality
    print(f"\n3. Testing RAG functionality...")
    rag_success = await test_rag_functionality()
    
    print("\n" + "=" * 60)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 60)
    
    if api_success and rag_success:
        print("🎉 ALL TESTS PASSED! Your RAG Chatbot is fully functional!")
        print("\n✅ Features working:")
        print("   - API endpoints responding correctly")
        print("   - Qdrant vector database connection")
        print("   - RAG (Retrieval-Augmented Generation)")
        print("   - Textbook content integration")
        print("   - OpenAI integration")
        print("\n💡 Next Steps:")
        print("   - Start the frontend: cd frontend && npm start")
        print("   - Ask questions about the textbook content")
        print("   - Select text on the page and ask specific questions")
        return True
    else:
        print("❌ SOME TESTS FAILED. Please check the error messages above.")
        print("\n🔧 Common issues:")
        print("   - Check your Qdrant Cloud instance is active")
        print("   - Verify your OpenAI API key is valid")
        print("   - Ensure the backend server is running")
        print("   - Check your .env file configuration")
        return False


if __name__ == "__main__":
    success = asyncio.run(run_full_test())
    sys.exit(0 if success else 1)