"""
from os import getenv


API_ID = int(getenv("API_ID", "16253557"))
API_HASH = getenv("API_HASH", "81171c25e4cb9062cb10da8b7730432a")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "1996039956"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1996039956").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://MRDAXX:MRDAXX@mrdaxx.prky3aj.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002281623908"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002363250260"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "16253557"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "81171c25e4cb9062cb10da8b7730432a")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8073120982:AAGgJI30ZBgsVmVWXz9c0Bi-vJv75pSR84Y")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("UGExtractorBot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "7463601722"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7463601722").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002601604234"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://jaydevswebpannel:jaydevgadhvi@core.efzs6h3.mongodb.net/?retryWrites=true&w=majority&appName=Core")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002601604234"))

