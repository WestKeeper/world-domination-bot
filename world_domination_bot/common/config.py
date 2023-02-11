import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


# Environment variables
TOKEN_API = os.getenv('TELEGRAM_BOT_TOKEN_API', '')

# Database constants
ROOT_DIR = Path(__file__).resolve().parent.parent
SQLITE_DB_FILE = ROOT_DIR / 'db.sqlite3'
TO_GENERATE_AND_DROP_DB = True

# Templates constants
TEMPLATES_DIR = ROOT_DIR / 'templates'
