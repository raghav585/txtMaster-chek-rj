import os

API_ID = API_ID = 21567814

API_HASH = os.environ.get("API_HASH", "cd7dc5431d449fd795683c550d7bfb7e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7656305851:AAF-VrDbuvSIX8pFJ8qnmoj993B50AU67fk")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6126688051))

LOG = -1002146213576

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6126688051").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
