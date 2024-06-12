# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 23653093 # integer value, dont use ""
    API_HASH = "ee6df88753c36eeab95391940ba3844f"
    TOKEN = "7155707387:AAH_P1y4qh2mwsyp-nMDIJHd1OWT7_Z8M1U"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = "1556830659" # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "lochakpochak"
    SUPPORT_CHAT = "its_witch_here"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001603027566
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001603027566
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://kalpanapreethiney:Ez4Xke7VUm4VQFAr@cluster0.hsx1cck.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # RECOMMENDED
    DATABASE_URL = "postgres://kkxqgoio:v60qxDjtyQFM_D26iV7g1zzejlYzmIas@silly.db.elephantsql.com/kkxqgoio"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "ZqWM2aI73puW4krk2lPnjz_SM0eC~q_nFxpGU066kJKUjU4fKMecVLt0sNFHBWNs"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = ("6049338121")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = ("6049338121")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = ("6049338121")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = ("6049338121")
    WOLVES = ("whitelists")
    DONATION_LINK = "https://t.me/lochakpochak" # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_CHATS = True
    DEL_CMDS = True
    INFOPIC = True
    STRICT_GBAN = True
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "D5UJD8IQE34NXJ0O"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "F8NYGXSAEEC4"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        ""  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
