import os
import sys

# 1. Add the parent directory to sys.path so we can import 'main'
# This allows 'from main import app' to work even though main.py is up one level
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# 2. Import the FastAPI app from your existing main.py
from main import app

# 3. This 'app' variable is what Vercel looks for to handle requests
