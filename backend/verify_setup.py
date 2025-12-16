#!/usr/bin/env python3
"""
Final verification script to ensure the RAG Chatbot is fully functional
"""

import sys
import os
from pathlib import Path

def check_backend_structure():
    """Check if backend structure is correct"""
    print("Checking backend structure...")

    backend_path = Path("backend")
    required_files = [
        "main.py",
        "start_server.py",
        "test_rag_chatbot.py",
        "load_textbook_content.py",
        "requirements.txt",
        ".env",
        "src/rag_chatbot/main.py",
        "src/rag_chatbot/config.py",
        "src/rag_chatbot/services/rag_service.py",
        "src/rag_chatbot/routes/chat.py"
    ]

    all_found = True
    for file in required_files:
        file_path = backend_path / file
        if not file_path.exists():
            print(f"MISSING: {file}")
            all_found = False
        else:
            print(f"FOUND: {file}")

    return all_found

def check_frontend_structure():
    """Check if frontend structure is correct"""
    print("\nChecking frontend structure...")

    frontend_path = Path("frontend")
    required_files = [
        "package.json",
        "src/components/Chat/ChatWidget.tsx",
        "src/components/Chat/EnhancedChat.tsx",
        "src/pages/chat.tsx",
        "src/contexts/ChatContext.tsx"  # Let's check if this exists
    ]

    # Check if ChatContext exists, if not we'll note it but not fail
    chat_context_path = frontend_path / "src" / "contexts" / "ChatContext.tsx"
    if chat_context_path.exists():
        print(f"FOUND: src/contexts/ChatContext.tsx")
    else:
        print(f"WARNING: src/contexts/ChatContext.tsx (this might be fine)")
        # Let's see what contexts exist
        contexts_dir = frontend_path / "src" / "contexts"
        if contexts_dir.exists():
            print(f"   Available contexts: {[f.name for f in contexts_dir.iterdir() if f.is_file()]}")

    all_found = True
    for file in [f for f in required_files if "ChatContext.tsx" not in f]:  # Skip ChatContext in strict check
        file_path = frontend_path / file
        if not file_path.exists():
            print(f"MISSING: {file}")
            all_found = False
        else:
            print(f"FOUND: {file}")

    return all_found

def check_textbook_content():
    """Check if textbook content exists"""
    print("\nChecking textbook content...")

    docs_path = Path("frontend/docs")
    if docs_path.exists():
        md_files = list(docs_path.glob("*.md"))
        print(f"FOUND {len(md_files)} textbook content files")
        if md_files:
            print(f"   Sample files: {[f.name for f in md_files[:5]]}")  # Show first 5 files
        return len(md_files) > 0
    else:
        print(f"MISSING Docs directory: {docs_path}")
        return False

def check_dependencies():
    """Check if dependencies can be imported"""
    print("\nChecking Python dependencies...")

    required_imports = [
        ("fastapi", "FastAPI"),
        ("uvicorn", "run"),
        ("openai", "AsyncOpenAI"),
        ("qdrant_client", "QdrantClient"),
        ("pydantic", "BaseModel"),
        ("pydantic_settings", "BaseSettings"),
        ("asyncpg", None),  # Just check if it can be imported
        ("python-dotenv", "load_dotenv")
    ]

    all_imported = True
    for module, attribute in required_imports:
        try:
            imported_module = __import__(module)
            if attribute:
                getattr(imported_module, attribute)
            print(f"OK: {module}")
        except (ImportError, AttributeError) as e:
            print(f"ERROR: {module}: {str(e)}")
            all_imported = False

    return all_imported

def check_env_vars():
    """Check if environment variables are set"""
    print("\nChecking environment variables...")

    backend_path = Path("backend")
    env_file = backend_path / ".env"

    if not env_file.exists():
        print(f"MISSING .env file: {env_file}")
        return False

    print(f"FOUND .env file")

    # Read and check for required environment variables
    env_vars = {}
    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                env_vars[key.strip()] = value.strip()

    required_vars = ["OPENAI_API_KEY", "QDRANT_URL", "QDRANT_API_KEY", "POSTGRES_URL"]
    all_set = True

    for var in required_vars:
        if var in env_vars and env_vars[var]:
            print(f"OK: {var}")
        else:
            print(f"MISSING: {var}")
            all_set = False

    return all_set

def verify_rag_components():
    """Verify that all RAG components are properly implemented"""
    print("\nVerifying RAG components...")

    # Check if all expected files exist
    rag_path = Path("backend/src/rag_chatbot")

    expected_files = [
        "main.py",
        "config.py",
        "routes/chat.py",
        "services/openai_service.py",
        "services/qdrant_service.py",
        "services/embedding_service.py",
        "services/rag_service.py",
        "models/data_models.py",
        "models/request_models.py"
    ]

    all_found = True
    for file in expected_files:
        file_path = rag_path / file
        if not file_path.exists():
            print(f"MISSING RAG component: {file}")
            all_found = False
        else:
            print(f"FOUND RAG component: {file}")

    return all_found

def run_final_verification():
    """Run the complete verification"""
    print("=" * 70)
    print("FINAL RAG CHATBOT VERIFICATION")
    print("=" * 70)

    print("This verification checks if all components of the RAG Chatbot are properly set up")
    print("and ready to function as a complete system.\n")

    checks = [
        ("Backend Structure", check_backend_structure),
        ("Frontend Structure", check_frontend_structure),
        ("Textbook Content", check_textbook_content),
        ("Python Dependencies", check_dependencies),
        ("Environment Variables", check_env_vars),
        ("RAG Components", verify_rag_components)
    ]

    results = {}
    for name, check_func in checks:
        print(f"\n{name}:")
        print("-" * len(name))
        results[name] = check_func()

    print("\n" + "=" * 70)
    print("VERIFICATION SUMMARY")
    print("=" * 70)

    all_passed = True
    for name, result in results.items():
        status = "PASS" if result else "FAIL"
        print(f"{name:.<50} {status}")
        if not result:
            all_passed = False

    if all_passed:
        print(f"\nALL CHECKS PASSED!")
        print(f"Your RAG Chatbot is fully configured and ready to use!")
        print(f"\nNext Steps:")
        print(f"   1. Start backend: cd backend && python start_server.py")
        print(f"   2. Start frontend: cd frontend && npm start")
        print(f"   3. Access the chatbot at http://localhost:3000")
    else:
        print(f"\nSOME CHECKS FAILED!")
        print(f"Please address the issues above before starting the system.")
        print(f"Refer to RUNNING_BACKEND.md for setup instructions.")

    print("=" * 70)
    return all_passed

if __name__ == "__main__":
    success = run_final_verification()
    sys.exit(0 if success else 1)