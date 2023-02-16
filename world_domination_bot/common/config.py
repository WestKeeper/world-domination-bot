import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


# Environment variables
TOKEN_API = os.getenv('TELEGRAM_BOT_TOKEN_API', '')

# Database constants
ROOT_DIR = Path(__file__).resolve().parent.parent
SQLITE_DB_FILE = ROOT_DIR / 'db.sqlite3'
TO_GENERATE_AND_DROP_DB = False

# Templates constants
TEMPLATES_DIR = ROOT_DIR / 'templates'

# Modes constants
TEST_MODE = True

# Session constants
START_ECOLOGY_LEVEL = 90
START_BUILD_BOMBS_NUM = 0
START_DROP_BOMBS_NUM = 0
START_NUKE_TECH_NUM = 0
START_DEV_ECO_NUM = 0
