#!/usr/bin/env python3
"""
Simple script to load textbook content into ChromaDB for RAG functionality.
"""

import json
import os
import sys
from pathlib import Path

# Add the backend src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.rag_chatbot.services.embedding_service import EmbeddingService
from src.rag_chatbot.services.vector_store import VectorStoreService

def load_textbook_content():
    """Load textbook content into ChromaDB"""
    print("=" * 60)
    print("LOADING TEXTBOOK CONTENT INTO CHROMADB")
    print("=" * 60)
    
    # Initialize services
    print("\n[1/4] Initializing embedding service...")
    embedding_service = EmbeddingService()
    
    print("[2/4] Initializing vector store...")
    vector_store = VectorStoreService()
    
    # Load JSON content
    print("[3/4] Loading textbook content JSON...")
    json_path = Path(__file__).parent / "src" / "rag_chatbot" / "data" / "textbook_content.json"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    chapters = data.get("chapters", [])
    print(f"   Found {len(chapters)} chapters")
    
    # Process chapters
    print("[4/4] Processing sections and generating embeddings...")
    documents = []
    embeddings = []
    metadatas = []
    ids = []
    
    for chapter in chapters:
        chapter_id = chapter.get("id")
        chapter_title = chapter.get("title")
        chapter_order = chapter.get("order", 0)
        difficulty = chapter.get("difficulty", "Unknown")
        
        for section in chapter.get("sections", []):
            section_id = section.get("id")
            section_title = section.get("title")
            content = section.get("content")
            tags = section.get("tags", [])
            
            # Create document with context
            doc_text = f"""Chapter: {chapter_title}
Section: {section_title}
Content: {content}"""
            
            documents.append(doc_text)
            ids.append(section_id)
            
            # Create safe metadata (all values must be string, int, float, or bool)
            safe_metadata = {
                "chapter_id": chapter_id,
                "chapter_title": chapter_title,
                "chapter_order": chapter_order,
                "section_id": section_id,
                "section_title": section_title,
                "difficulty": difficulty,
                "tags": ", ".join(tags) if tags else ""
            }
            metadatas.append(safe_metadata)
    
    print(f"   Generated {len(documents)} document sections")
    
    # Generate embeddings
    print("\nGenerating embeddings (this may take a moment)...")
    try:
        embeddings = embedding_service.embed_texts(documents)
        print(f"   [OK] Generated {len(embeddings)} embeddings")
    except Exception as e:
        print(f"   [ERROR] Error generating embeddings: {e}")
        return False
    
    # Add to vector store
    print("Adding documents to ChromaDB...")
    try:
        vector_store.add_documents(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        print("   [OK] Documents added successfully")
    except Exception as e:
        print(f"   [ERROR] Error adding documents: {e}")
        return False
    
    # Get stats
    stats = vector_store.get_collection_stats()
    
    print("\n" + "=" * 60)
    print("[SUCCESS] CONTENT LOADED SUCCESSFULLY!")
    print("=" * 60)
    print(f"\nCollection Stats:")
    print(f"   Total documents: {stats.get('total_documents', len(documents))}")
    print(f"   Chapters processed: {len(chapters)}")
    print(f"   Sections indexed: {len(documents)}")
    
    print("\nThe chatbot can now answer questions about:")
    for chapter in chapters[:5]:
        print(f"   - {chapter['title']}")
    if len(chapters) > 5:
        print(f"   - ... and {len(chapters) - 5} more chapters")
    
    print("\nNext steps:")
    print("   1. Start backend: python main.py")
    print("   2. Start frontend: cd frontend && npm start")
    print("   3. Ask questions like 'What is Physical AI?' or 'Explain ZMP'")
    
    return True

if __name__ == "__main__":
    try:
        success = load_textbook_content()
        if success:
            print("\n[DONE] Setup complete! Your RAG chatbot is ready.")
        else:
            print("\n[FAILED] Setup failed. Please check the errors above.")
            sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
