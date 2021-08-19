HEROKU = True # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["1915433179:AAHLg-WGh88qbFaU34T16w1MkW9KM0HYZlE"]
    ARQ_API_KEY = environ["OXGDGH-KBMDYC-SELQWI-ICSTWU-ARQ"]
    LANGUAGE = environ["en"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "1915433179:AAHLg-WGh88qbFaU34T16w1MkW9KM0HYZlE"
    ARQ_API_KEY = "Get this from @ARQRobot"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "en"

# Leave it as it is
ARQ_API_BASE_URL = "https://thearq.tech"
