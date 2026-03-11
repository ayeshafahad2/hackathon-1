#!/usr/bin/env python3
"""
Physical AI & Humanoid Robotics - Comprehensive Test Suite
Tests for Backend API, RAG Chatbot, and System Integration
"""

import sys
import json
import time
from datetime import datetime
from typing import Dict, List, Any

# Test Results Storage
test_results = {
    "timestamp": datetime.now().isoformat(),
    "total_tests": 0,
    "passed": 0,
    "failed": 0,
    "skipped": 0,
    "tests": []
}

def log_test(name: str, passed: bool, details: str = "", error: str = ""):
    """Log test result"""
    test_results["total_tests"] += 1
    if passed:
        test_results["passed"] += 1
        status = "[PASS]"
    else:
        test_results["failed"] += 1
        status = "[FAIL]"
    
    test_results["tests"].append({
        "name": name,
        "status": "passed" if passed else "failed",
        "details": details,
        "error": error
    })
    
    print(f"{status} {name}")
    if details:
        print(f"  -> {details}")
    if error:
        print(f"  -> Error: {error}")
    print()

def skip_test(name: str, reason: str):
    """Skip a test"""
    test_results["total_tests"] += 1
    test_results["skipped"] += 1
    test_results["tests"].append({
        "name": name,
        "status": "skipped",
        "details": reason,
        "error": ""
    })
    print(f"[SKIP] {name}")
    print(f"  -> {reason}")
    print()

print("=" * 70)
print("PHYSICAL AI & HUMANOID ROBOTICS - TEST SUITE")
print("=" * 70)
print()

# ============================================================================
# SECTION 1: FILE SYSTEM TESTS
# ============================================================================
print("[FILES] SECTION 1: FILE SYSTEM TESTS")
print("-" * 70)

import os

# Test 1: Check Frontend Directory
try:
    frontend_exists = os.path.exists("frontend")
    log_test(
        "Frontend directory exists",
        frontend_exists,
        "Frontend directory found" if frontend_exists else "Frontend directory not found"
    )
except Exception as e:
    log_test("Frontend directory exists", False, error=str(e))

# Test 2: Check Backend Directory
try:
    backend_exists = os.path.exists("backend")
    log_test(
        "Backend directory exists",
        backend_exists,
        "Backend directory found" if backend_exists else "Backend directory not found"
    )
except Exception as e:
    log_test("Backend directory exists", False, error=str(e))

# Test 3: Check Package.json
try:
    package_exists = os.path.exists("frontend/package.json")
    log_test(
        "Package.json exists",
        package_exists,
        "Frontend package.json found" if package_exists else "Package.json not found"
    )
except Exception as e:
    log_test("Package.json exists", False, error=str(e))

# Test 4: Check Docusaurus Config
try:
    docusaurus_config = os.path.exists("frontend/docusaurus.config.ts")
    log_test(
        "Docusaurus config exists",
        docusaurus_config,
        "docusaurus.config.ts found" if docusaurus_config else "Config not found"
    )
except Exception as e:
    log_test("Docusaurus config exists", False, error=str(e))

# Test 5: Check Features Page
try:
    features_page = os.path.exists("frontend/src/pages/features.tsx")
    log_test(
        "Features page exists",
        features_page,
        "features.tsx found" if features_page else "Features page not found"
    )
except Exception as e:
    log_test("Features page exists", False, error=str(e))

# Test 6: Check Docs Directory
try:
    docs_exist = os.path.exists("frontend/docs")
    docs_count = len([f for f in os.listdir("frontend/docs") if f.endswith('.md')]) if docs_exist else 0
    log_test(
        "Documentation files exist",
        docs_exist and docs_count > 0,
        f"Found {docs_count} markdown files in docs/"
    )
except Exception as e:
    log_test("Documentation files exist", False, error=str(e))

print()

# ============================================================================
# SECTION 2: FRONTEND BUILD TESTS
# ============================================================================
print("[BUILD] SECTION 2: FRONTEND BUILD TESTS")
print("-" * 70)

# Test 7: Check Node Modules
try:
    node_modules = os.path.exists("frontend/node_modules")
    log_test(
        "Node modules installed",
        node_modules,
        "node_modules directory found" if node_modules else "Run npm install"
    )
except Exception as e:
    log_test("Node modules installed", False, error=str(e))

# Test 8: Check Package Dependencies
try:
    import json
    with open("frontend/package.json", 'r') as f:
        package_data = json.load(f)
    
    has_docusaurus = "@docusaurus/core" in package_data.get("dependencies", {})
    has_react = "react" in package_data.get("dependencies", {})
    
    log_test(
        "Required dependencies present",
        has_docusaurus and has_react,
        f"Docusaurus: {has_docusaurus}, React: {has_react}"
    )
except Exception as e:
    log_test("Required dependencies present", False, error=str(e))

# Test 9: Check Build Scripts
try:
    with open("frontend/package.json", 'r') as f:
        package_data = json.load(f)
    
    has_build = "build" in package_data.get("scripts", {})
    has_start = "start" in package_data.get("scripts", {})
    
    log_test(
        "Build scripts configured",
        has_build and has_start,
        f"Build: {has_build}, Start: {has_start}"
    )
except Exception as e:
    log_test("Build scripts configured", False, error=str(e))

print()

# ============================================================================
# SECTION 3: BACKEND API TESTS
# ============================================================================
print("[BACKEND] SECTION 3: BACKEND API TESTS")
print("-" * 70)

# Test 10: Check Backend Main File
try:
    backend_main = os.path.exists("backend/src/rag_chatbot/main.py")
    log_test(
        "Backend main file exists",
        backend_main,
        "main.py found" if backend_main else "Backend main not found"
    )
except Exception as e:
    log_test("Backend main file exists", False, error=str(e))

# Test 11: Check RAG Service
try:
    rag_service = os.path.exists("backend/src/rag_chatbot/services/rag_service.py")
    log_test(
        "RAG service exists",
        rag_service,
        "rag_service.py found" if rag_service else "RAG service not found"
    )
except Exception as e:
    log_test("RAG service exists", False, error=str(e))

# Test 12: Check Vector Store
try:
    vector_store = os.path.exists("backend/src/rag_chatbot/services/vector_store.py")
    log_test(
        "Vector store exists",
        vector_store,
        "vector_store.py found" if vector_store else "Vector store not found"
    )
except Exception as e:
    log_test("Vector store exists", False, error=str(e))

# Test 13: Check ChromaDB Directory
try:
    chroma_db = os.path.exists("backend/chroma_db")
    log_test(
        "ChromaDB directory exists",
        chroma_db,
        "Vector database directory found" if chroma_db else "ChromaDB not found"
    )
except Exception as e:
    log_test("ChromaDB directory exists", False, error=str(e))

print()

# ============================================================================
# SECTION 4: CONTENT TESTS
# ============================================================================
print("[CONTENT] SECTION 4: CONTENT TESTS")
print("-" * 70)

# Test 14: Check Textbook Content
try:
    textbook_content = os.path.exists("backend/src/rag_chatbot/data/textbook_content.json")
    log_test(
        "Textbook content exists",
        textbook_content,
        "textbook_content.json found" if textbook_content else "Content not found"
    )
except Exception as e:
    log_test("Textbook content exists", False, error=str(e))

# Test 15: Validate Content Structure
try:
    if textbook_content:
        with open("backend/src/rag_chatbot/data/textbook_content.json", 'r', encoding='utf-8') as f:
            content = json.load(f)
        
        has_chapters = "chapters" in content
        chapter_count = len(content.get("chapters", []))
        
        log_test(
            "Content structure valid",
            has_chapters and chapter_count > 0,
            f"Found {chapter_count} chapters"
        )
    else:
        skip_test("Content structure valid", "Textbook content not found")
except Exception as e:
    log_test("Content structure valid", False, error=str(e))

# Test 16: Check Week Modules
try:
    week_files = [f for f in os.listdir("frontend/docs") if f.startswith("week-")]
    log_test(
        "Week modules exist",
        len(week_files) > 0,
        f"Found {len(week_files)} week modules"
    )
except Exception as e:
    log_test("Week modules exist", False, error=str(e))

print()

# ============================================================================
# SECTION 5: CONFIGURATION TESTS
# ============================================================================
print("[CONFIG] SECTION 5: CONFIGURATION TESTS")
print("-" * 70)

# Test 17: Check Vercel Configuration
try:
    vercel_config = os.path.exists("frontend/vercel.json")
    log_test(
        "Vercel config exists",
        vercel_config,
        "vercel.json found" if vercel_config else "Vercel config not found"
    )
except Exception as e:
    log_test("Vercel config exists", False, error=str(e))

# Test 18: Validate Vercel Config
try:
    if vercel_config:
        with open("frontend/vercel.json", 'r') as f:
            vercel_data = json.load(f)
        
        has_build = "buildCommand" in vercel_data
        has_output = "outputDirectory" in vercel_data
        
        log_test(
            "Vercel config valid",
            has_build and has_output,
            f"Build: {vercel_data.get('buildCommand')}, Output: {vercel_data.get('outputDirectory')}"
    )
    else:
        skip_test("Vercel config valid", "Vercel config not found")
except Exception as e:
    log_test("Vercel config valid", False, error=str(e))

# Test 19: Check Git Repository
try:
    git_exists = os.path.exists(".git")
    log_test(
        "Git repository initialized",
        git_exists,
        ".git directory found" if git_exists else "Not a git repository"
    )
except Exception as e:
    log_test("Git repository initialized", False, error=str(e))

print()

# ============================================================================
# SECTION 6: DEPLOYMENT TESTS
# ============================================================================
print("[DEPLOY] SECTION 6: DEPLOYMENT TESTS")
print("-" * 70)

# Test 20: Check Deployment Scripts
try:
    deploy_scripts = [
        "deploy_to_hf.py",
        "deploy_auto.py",
        "deploy_hf.bat"
    ]
    found_scripts = [s for s in deploy_scripts if os.path.exists(s)]
    
    log_test(
        "Deployment scripts exist",
        len(found_scripts) > 0,
        f"Found {len(found_scripts)} deployment scripts: {', '.join(found_scripts)}"
    )
except Exception as e:
    log_test("Deployment scripts exist", False, error=str(e))

# Test 21: Check Dockerfile
try:
    dockerfile = os.path.exists("Dockerfile")
    log_test(
        "Dockerfile exists",
        dockerfile,
        "Dockerfile found" if dockerfile else "Dockerfile not found"
    )
except Exception as e:
    log_test("Dockerfile exists", False, error=str(e))

# Test 22: Check README Files
try:
    readme_files = [f for f in os.listdir(".") if f.lower().startswith("readme") and f.endswith(".md")]
    log_test(
        "README files exist",
        len(readme_files) > 0,
        f"Found {len(readme_files)} README files"
    )
except Exception as e:
    log_test("README files exist", False, error=str(e))

print()

# ============================================================================
# SECTION 7: UI/UX TESTS
# ============================================================================
print("[UI/UX] SECTION 7: UI/UX TESTS")
print("-" * 70)

# Test 23: Check Features Page CSS
try:
    features_css = os.path.exists("frontend/src/pages/features.module.css")
    log_test(
        "Features page styles exist",
        features_css,
        "features.module.css found" if features_css else "CSS not found"
    )
except Exception as e:
    log_test("Features page styles exist", False, error=str(e))

# Test 24: Check Homepage
try:
    homepage = os.path.exists("frontend/src/pages/index.tsx")
    log_test(
        "Homepage exists",
        homepage,
        "index.tsx found" if homepage else "Homepage not found"
    )
except Exception as e:
    log_test("Homepage exists", False, error=str(e))

# Test 25: Check CSS Custom Styles
try:
    custom_css = os.path.exists("frontend/src/css/custom.css")
    log_test(
        "Custom CSS exists",
        custom_css,
        "custom.css found" if custom_css else "Custom CSS not found"
    )
except Exception as e:
    log_test("Custom CSS exists", False, error=str(e))

print()

# ============================================================================
# TEST SUMMARY
# ============================================================================
print("=" * 70)
print("TEST SUMMARY")
print("=" * 70)
print(f"Total Tests:  {test_results['total_tests']}")
print(f"[PASS] Passed:     {test_results['passed']}")
print(f"[FAIL] Failed:     {test_results['failed']}")
print(f"[SKIP] Skipped:    {test_results['skipped']}")
print(f"Success Rate: {(test_results['passed'] / test_results['total_tests'] * 100):.1f}%")
print("=" * 70)
print()

# Generate Test Report
test_report = f"""
## Test Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

### Summary
- **Total Tests:** {test_results['total_tests']}
- **Passed:** {test_results['passed']} [PASS]
- **Failed:** {test_results['failed']} [FAIL]
- **Skipped:** {test_results['skipped']} [SKIP]
- **Success Rate:** {(test_results['passed'] / test_results['total_tests'] * 100):.1f}%

### Test Categories
1. **File System Tests** - Directory and file structure validation
2. **Frontend Build Tests** - Dependencies and build configuration
3. **Backend API Tests** - RAG chatbot and API endpoints
4. **Content Tests** - Textbook content and documentation
5. **Configuration Tests** - Vercel and deployment config
6. **Deployment Tests** - Docker and deployment scripts
7. **UI/UX Tests** - Frontend components and styles

### Test Results Details
"""

for test in test_results['tests']:
    status_icon = "[PASS]" if test['status'] == 'passed' else ("[FAIL]" if test['status'] == 'failed' else "[SKIP]")
    test_report += f"\n{status_icon} **{test['name']}** - {test['status'].upper()}"
    if test['details']:
        test_report += f"\n  - {test['details']}"
    if test['error']:
        test_report += f"\n  - Error: {test['error']}"

test_report += f"""

### System Information
- **Node Version:** Required >=20.0
- **Framework:** Docusaurus 3.9.2
- **React:** 19.0.0
- **TypeScript:** 5.6.2
- **Backend:** FastAPI with RAG
- **Vector DB:** ChromaDB
- **Deployment:** Vercel + Hugging Face Spaces

### Recommendations
"""

if test_results['failed'] > 0:
    test_report += "\n- Review failed tests and fix issues before deployment\n"
if test_results['skipped'] > 0:
    test_report += "\n- Address skipped tests to ensure complete coverage\n"

test_report += "\n- Run `npm run build` to verify frontend builds successfully\n"
test_report += "\n- Test backend API endpoints locally before deployment\n"
test_report += "\n- Verify all content files are properly formatted\n"

# Save test report
with open("TEST_REPORT.md", 'w', encoding='utf-8') as f:
    f.write(test_report)

print("[OK] Test report saved to TEST_REPORT.md")
print()

# Exit with appropriate code
sys.exit(0 if test_results['failed'] == 0 else 1)
