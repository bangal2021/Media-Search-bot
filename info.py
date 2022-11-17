import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = 'LeoMediaSearchBot'
USER_SESSION = 'User_Bot'
API_ID = 1706730
API_HASH = '14a483d10b9191f077e1a954a131c59e'
BOT_TOKEN = '5690605277:AAF6P6mJubgwbB5FhWfPwL3TQgUANZj9RPs'

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = ['@ravi00893']
CHANNELS = [-1001840839823]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = -1001840839823
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = "mongodb+srv://cinee:cinee@cluster0.d5aveoz.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = 'cinee'
COLLECTION_NAME = 'channel_files'

# Messages
default_start_msg = """
**Hi, I'm Media Search Bot or ypu can call me as Auto-Filter Bot**
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = "cca8a5e"
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
