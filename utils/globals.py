from typing import Final
from utils.config import Config
from utils.logger import Logger

# ---- Regexes ---- #
# Regex to find the raw gif URL from a Tenor URL (they provide a link to a page with the gif embedded within the HTML)
TENOR_REGEX = r"(?i)\b((https?://media1[.]tenor[.]com/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))[.]gif)"
ALT_TENOR_REGEX = r"(?i)\b((https?://c[.]tenor[.]com/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))[.]gif)"
CLEAN_URL_REGEX = r"\?.*$" # Regex to remove all parameters from a URL (solely used to check to see if a url ends in .gif, probably a better way but meh)


# ---- Misc ---- #
POST_HR_INTERVAL = 4
GIF_SIZE_LIMIT = 10000000 # Mastodon's file size limit is 10MB
CATBOX_URL = "https://catbox.moe/user/api.php" # Catbox.moe API URL
CAT_HASHTAGS = ['gifkitties', 'cat', 'catlife', 'catlove', 'catlover', 'catlovers', 'catoftheday', 'cats', 'catsoftheworld', 'catgif', 'catgifs', 'gifs', 'gif'] # Cat related hashtags
cfg = Config(path = "config.json") # Config class instance
log = Logger() # Logger


# ---- Webhook information ---- #
# Information for the post notification webhook
POST_WB_INFO: Final = {
	"username": "@gifkitties",
	"pfp": "https://pbs.twimg.com/profile_images/3424946333/6ead4754bb47e8ec302c1d536cb693b1_reasonably_small.gif"
}

# Information for the misc notification webhook (sent to theserver where tweets are posted from)
MISC_WB_INFO: Final = {
	"username": "Tweet Bot",
	"pfp": "https://cdn.discordapp.com/avatars/980746909222338580/840892f27a807f8ad37ed1f23f56d95d.webp"
}


# ---- Requests ---- #
# Base browser headers for requests
BASE_HEADERS: Final = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
	"Accept": "*/*",
	"Accept-Encoding": "gzip, deflate, br",
	"Connection": "keep-alive",
}
