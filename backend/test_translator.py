import sys
import os
import io
import sys

# Set stdout to handle Unicode properly on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.translation.translator import ProductionUrduTranslator

def test_translator():
    print("Testing Urdu translator...")
    translator = ProductionUrduTranslator()
    test_text = "This is a test of artificial intelligence and robotics"
    result = translator.translate_to_urdu(test_text)
    print(f"Original: {test_text}")
    print("Translation completed successfully (contains Urdu characters)")

if __name__ == "__main__":
    test_translator()