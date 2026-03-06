import sys
import os
import io

# Set stdout to handle Unicode properly on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.auth.database import init_db

def test_db():
    print('Initializing database...')
    init_db()
    print('Database initialized successfully!')

if __name__ == '__main__':
    test_db()