#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29765293"))
API_HASH = environ.get("API_HASH", "97d072028ac81567a07ba0e8094375cc")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "7534974202"))
CREDIT = "✴★𝓝𝓞𝓣𝓗𝓘𝓝𝓖★✴"
AUTH_USER = os.environ.get('AUTH_USERS', '7534974202').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
