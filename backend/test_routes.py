#!/usr/bin/env python3
"""
Test script to check if routes are loading properly
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    print("Testing individual imports...")

    try:
        from src.rag_chatbot.main import app
        print("[OK] Main app imported successfully")
    except Exception as e:
        print(f"[ERROR] Error importing main app: {e}")
        return False

    try:
        from src.auth.routes import router as auth_router
        print("[OK] Auth routes imported successfully")
    except Exception as e:
        print(f"[ERROR] Error importing auth routes: {e}")
        return False

    try:
        from src.personalization.routes import router as personalization_router
        print("[OK] Personalization routes imported successfully")
    except Exception as e:
        print(f"[ERROR] Error importing personalization routes: {e}")
        return False

    try:
        from src.translation.routes import router as translation_router
        print("[OK] Translation routes imported successfully")
    except Exception as e:
        print(f"[ERROR] Error importing translation routes: {e}")
        return False

    try:
        app.include_router(auth_router, prefix='/api/v1')
        print("[OK] Auth routes included successfully")
    except Exception as e:
        print(f"[ERROR] Error including auth routes: {e}")
        return False

    try:
        app.include_router(personalization_router, prefix='/api/v1/personalization')
        print("[OK] Personalization routes included successfully")
    except Exception as e:
        print(f"[ERROR] Error including personalization routes: {e}")
        return False

    try:
        app.include_router(translation_router, prefix='/api/v1/translation')
        print("[OK] Translation routes included successfully")
    except Exception as e:
        print(f"[ERROR] Error including translation routes: {e}")
        return False

    print("\nAll imports completed successfully!")

    # Check routes
    print("\nAvailable routes in the app:")
    for route in app.routes:
        methods = getattr(route, 'methods', ['UNKNOWN'])
        path = getattr(route, 'path', 'UNKNOWN_PATH')
        name = getattr(route, 'name', 'UNKNOWN_NAME')
        print(f'  {methods} {path} ({name})')

    return True

if __name__ == "__main__":
    test_imports()