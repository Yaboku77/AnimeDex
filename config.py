# Your TechZ Api Key
# Get from @TechZApiBot on Telegram | https://t.me/TechZApiBot

from os import getenv


API_KEY = "WNWXNV"

if not API_KEY or API_KEY == "WNWXNV" or API_KEY == "WNWXNV":
    API_KEY = getenv("WNWXNV")

    if not API_KEY:
        raise Exception("Please add your TechZ Api Key in config.py file")
