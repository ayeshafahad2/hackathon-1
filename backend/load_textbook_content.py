#!/usr/bin/env python3
"""
Script to load textbook content into the Qdrant vector database for RAG functionality.
This will make the chatbot smart and able to answer questions about the book.
"""

import asyncio
import os
import sys
import glob
from pathlib import Path
import re

# Add the backend src directory to the path so imports work
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.rag_chatbot.models.data_models import Document
from src.rag_chatbot.services.rag_service import RAGService
from src.rag_chatbot.services.embedding_service import EmbeddingService
from src.rag_chatbot.config import settings

def clean_markdown_content(content: str) -> str:
    """
    Clean markdown content by removing headers and other formatting that might not be useful for RAG
    """
    # Remove markdown headers but keep the content
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Skip empty lines and header lines
        if line.strip() and not line.startswith('#'):
            cleaned_lines.append(line.strip())
    
    # Join the lines back together
    cleaned_content = '\n'.join(cleaned_lines)
    
    # Remove extra whitespace
    cleaned_content = re.sub(r'\n\s*\n', '\n\n', cleaned_content)
    
    return cleaned_content.strip()

async def load_textbook_content():
    """
    Load textbook content from markdown files into the RAG system
    """
    print("Loading textbook content into RAG system...")
    
    # Check if Qdrant is available
    rag_service = RAGService()
    
    if not rag_service.qdrant_available:
        print("❌ Qdrant is not available. Please check your Qdrant configuration in the .env file.")
        print(f"   Current Qdrant URL: {settings.qdrant_url}")
        print(f"   Qdrant API Key is set: {'Yes' if settings.qdrant_api_key else 'No'}")
        
        # Attempt to initialize Qdrant manually to see the error
        from src.rag_chatbot.services.qdrant_service import QdrantService
        qdrant_service = QdrantService()
        
        if not qdrant_service.client:
            print("❌ Failed to connect to Qdrant. The chatbot will work but won't have access to textbook content.")
            print("   Please verify your Qdrant credentials and try again.")
            return False
    
    print("✅ Qdrant is available!")
    
    # Find all markdown files in the docs directory
    docs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend', 'docs')
    markdown_files = glob.glob(os.path.join(docs_dir, '*.md'))
    
    if not markdown_files:
        print(f"❌ No markdown files found in {docs_dir}")
        return False
    
    print(f"📚 Found {len(markdown_files)} textbook content files")
    
    total_documents_added = 0
    
    for md_file in markdown_files:
        try:
            print(f"Processing: {os.path.basename(md_file)}")
            
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract a meaningful title from the file
            title_match = re.match(r'#\s+(.+)', content)
            title = title_match.group(1) if title_match else os.path.basename(md_file, '.md')
            
            # Clean the content for better RAG performance
            cleaned_content = clean_markdown_content(content)
            
            # Only add content if it's substantial
            if len(cleaned_content.strip()) > 50:
                # Create a document
                doc = Document(
                    id=f"{title.replace(' ', '_')}_{hash(cleaned_content) % 10000}",
                    content=cleaned_content,
                    metadata={
                        "title": title,
                        "source_file": os.path.basename(md_file),
                        "section": os.path.splitext(os.path.basename(md_file))[0],
                        "type": "textbook_content"
                    }
                )
                
                # Add the document to the RAG system
                success = await rag_service.add_document(doc)
                
                if success:
                    print(f"   ✅ Successfully added: {title}")
                    total_documents_added += 1
                else:
                    print(f"   ❌ Failed to add: {title}")
            else:
                print(f"   ⚠️  Skipping {title} - content too short")
                
        except Exception as e:
            print(f"   ❌ Error processing {md_file}: {str(e)}")
    
    print(f"\n🎉 Completed! Added {total_documents_added} documents to the RAG system.")
    print("🤖 The chatbot is now smart and can answer questions about the textbook content!")
    
    return True

def test_qdrant_connection():
    """
    Test the Qdrant connection separately to troubleshoot connection issues
    """
    print("Testing Qdrant connection...")
    
    try:
        from qdrant_client import QdrantClient
        from urllib.parse import urlparse
        
        # Parse the URL to determine the right connection method
        qdrant_url = settings.qdrant_url
        qdrant_api_key = settings.qdrant_api_key
        
        print(f"Qdrant URL: {qdrant_url}")
        
        # Determine if this is a cloud instance
        if 'cloud.qdrant.io' in qdrant_url:
            print("Detected Qdrant Cloud instance")
            parsed = urlparse(qdrant_url)
            host = parsed.hostname
            port = parsed.port or 443
            
            print(f"Connecting to host: {host}, port: {port}")
            
            client = QdrantClient(
                host=host,
                port=port,
                grpc_port=-1,
                api_key=qdrant_api_key,
                https=True,
                check_compatibility=False
            )
        elif qdrant_url.startswith('https://') or qdrant_url.startswith('http://'):
            print("Using direct URL connection")
            client = QdrantClient(
                url=qdrant_url,
                api_key=qdrant_api_key,
                https=qdrant_url.startswith('https://'),
                check_compatibility=False
            )
        else:
            print("Using host/port connection")
            client = QdrantClient(
                host=qdrant_url,
                api_key=qdrant_api_key,
                check_compatibility=False
            )
        
        # Test the connection
        collections = client.get_collections()
        print(f"✅ Qdrant connection successful!")
        print(f"   Available collections: {[col.name for col in collections.collections]}")
        
        return True
        
    except Exception as e:
        print(f"❌ Qdrant connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    # First, test the Qdrant connection
    print("=" * 60)
    print("QDRANT CONNECTION TEST")
    print("=" * 60)
    
    connection_ok = test_qdrant_connection()
    
    if not connection_ok:
        print("\n⚠️  Qdrant connection failed - attempting fixes...")
        # If connection fails, suggest fixes
        print("\nTroubleshooting tips:")
        print("1. Verify your Qdrant URL and API key in the .env file")
        print("2. Check if your Qdrant cluster is active in the Qdrant Cloud dashboard")
        print("3. Ensure the API key has sufficient permissions")
        print("4. Check your firewall/internet connection")
        
        # Exit early if connection fails
        exit(1)
    
    print("\n" + "=" * 60)
    print("LOADING TEXTBOOK CONTENT")
    print("=" * 60)
    
    # Now load the textbook content
    success = asyncio.run(load_textbook_content())
    
    if success:
        print("\n🚀 Everything is set up! The chatbot can now answer questions about the textbook.")
        print("\nTo test the chatbot:")
        print("1. Make sure your backend is running: python main.py")
        print("2. Start the frontend: cd frontend && npm start")
        print("3. Ask questions like 'What is Physical AI?' or 'Tell me about ROS 2'")
    else:
        print("\n❌ There were issues loading the content. Please resolve them and try again.")