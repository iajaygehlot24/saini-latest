#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "10634878"))
API_HASH = environ.get("API_HASH", "2eab99b8459017fff27395cc52f3c860")
BOT_TOKEN = environ.get("BOT_TOKEN", "7639873220:AAGrG84WtMkIJ0HjfOBkfPpY0cpU4R0swsc")
OWNER = int(environ.get("OWNER", "1168219996"))
CREDIT = environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")
AUTH_USER = os.environ.get('AUTH_USERS', '1168219996').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
