from dotenv import load_dotenv
from os import getenv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DOTENV_PATH = BASE_DIR / '.env'

if DOTENV_PATH.exists():
    load_dotenv(DOTENV_PATH)

API_TOKEN = getenv('API_TOKEN')

# Paths config
USERS_JSON_PATH = BASE_DIR / 'users.json'
ROUTES_PATH = BASE_DIR / 'tutu_routes.csv'

if not USERS_JSON_PATH.exists():
    with open(USERS_JSON_PATH, 'x') as users_json:
        users_json.write('{}')
