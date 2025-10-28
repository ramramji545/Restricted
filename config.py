# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "26331872"))
API_HASH = getenv("API_HASH", "c93589620441707c37c5683a02eea54e")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8355707251").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ajmerasaini01:U1sGiZRI6Ha0xuCy@cluster0.tnok3d0.mongodb.net/")
LOG_GROUP = getenv("LOG_GROUP", "-1003094137825")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003094137825"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "99999933273273737357357357"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "99999999999773737357537327349999"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
