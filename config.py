import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "29273649"))
API_HASH = environ.get("API_HASH", "0e4cebacaaebe9d618b5a5360d40e684")
BOT_TOKEN = environ.get("BOT_TOKEN", "7728618006:AAFYiUl-xlQmGqlmDvG-L5jRa9mq5eFrpfQ")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "2624154172"))
ADMINS = int(environ.get("ADMINS", "8163557664"))
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
