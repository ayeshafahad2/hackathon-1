import requests
import sys

print("Testing Backend Connection...")
print("=" * 60)

# Test 1: Health endpoint
print("\n1. Testing Health Endpoint...")
try:
    response = requests.get("https://Ayeshaaabir-physical-ai-backend.hf.space/health", timeout=15)
    print(f"   Status Code: {response.status_code}")
    print(f"   Response: {response.json()}")
    if response.status_code == 200:
        print("   ✅ Backend is RUNNING!")
    else:
        print("   ⚠️ Backend returned error")
except requests.exceptions.Timeout:
    print("   ❌ TIMEOUT - Backend not responding")
except requests.exceptions.ConnectionError as e:
    print(f"   ❌ CONNECTION ERROR: {e}")
except Exception as e:
    print(f"   ❌ ERROR: {e}")

# Test 2: Chat endpoint
print("\n2. Testing Chat Endpoint...")
try:
    response = requests.post(
        "https://Ayeshaaabir-physical-ai-backend.hf.space/api/v1/chat",
        json={"message": "What is Physical AI?"},
        timeout=15
    )
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"   Response: {data.get('response', '')[:100]}...")
        print("   ✅ Chat is WORKING!")
    else:
        print(f"   ❌ Chat returned error: {response.text[:200]}")
except requests.exceptions.Timeout:
    print("   ❌ TIMEOUT - Chat endpoint not responding")
except Exception as e:
    print(f"   ❌ ERROR: {e}")

print("\n" + "=" * 60)
print("Test Complete!")
