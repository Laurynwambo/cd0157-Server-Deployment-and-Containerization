from dotenv import load_dotenv
import os
load_dotenv()

SECRET = os.environ.get("SECRET")
TOKEN = os.environ.get("TOKEN")
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
JWT_SECRET = os.environ.get('JWT_SECRET', 'abc123abc1234')
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')