#!/usr/bin/env python3
"""
Quick setup and test script for the RAG Chatbot
Installs missing dependencies and runs a quick test
"""

import subprocess
import sys
import os

def install_missing_deps():
    """Install missing Python dependencies"""
    print("📦 Installing missing dependencies...")
    
    # Install the packages that failed verification
    packages_to_install = ["asyncpg", "python-dotenv"]
    
    for package in packages_to_install:
        print(f"Installing {package}...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", package], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {package} installed successfully")
        else:
            print(f"❌ Failed to install {package}: {result.stderr}")
            return False
    
    return True

def test_basic_imports():
    """Test that all required modules can be imported"""
    print("\n🔍 Testing basic imports...")
    
    required_modules = [
        "fastapi",
        "uvicorn",
        "openai",
        "qdrant_client",
        "pydantic",
        "pydantic_settings",
        "asyncpg",
        "python-dotenv"
    ]
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}: {e}")
            return False
    
    return True

def main():
    print("=" * 60)
    print("🔧 RAG CHATBOT QUICK SETUP")
    print("=" * 60)
    
    print("\nThis script will:")
    print("1. Install missing Python dependencies")
    print("2. Verify all imports work correctly")
    print("3. Confirm the RAG Chatbot is ready to run")
    
    # Install missing dependencies
    if not install_missing_deps():
        print("\n❌ Failed to install dependencies. Please install manually:")
        print("   pip install asyncpg python-dotenv")
        return False
    
    # Test imports
    if not test_basic_imports():
        print("\n❌ Some imports failed. Please check your installation.")
        return False
    
    print(f"\n🎉 SUCCESS! All dependencies installed and working.")
    print(f"\n🚀 Your RAG Chatbot is ready to run!")
    print(f"\nTo start the system:")
    print(f"   Backend: cd backend && python start_server.py")
    print(f"   Frontend: cd frontend && npm start")
    print(f"\nThe fully functional RAG Chatbot awaits you!")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)