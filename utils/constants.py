from typing import Final

# ---- Regexes ---- #
# Regex to find the raw gif URL from a Tenor URL (they provide a link to a page with the gif embedded within the HTML)
TENOR_REGEX = r"(?i)\b((https?://media[.]tenor[.]com/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))[.]gif)"

# Regex to remove all parameters from a URL (solely used to check to see if a url ends in .gif, probably a better way but meh)
CLEAN_URL_REGEX = r"\?.*$"


# ---- Misc ---- #
# Twitter's file size limit is 15MB, this is in bytes
FILESIZE_LIMIT_TWITTER = 15728640

# Catbox.moe API URL
CATBOX_URL = "https://catbox.moe/user/api.php"

# Default configuration file
DEFAULT_CFG: Final = {
	"userhash": "enter a randomly generated string here",
	"discord": {
		"token": "",
		"post_notifs": {
			"enabled": True,
			"webhook": "",
			"role_to_ping": "",
		},
		"misc_notifs": {
			"enabled": True,
			"webhook": "",
		},
		"authed_users": [],
		"emojis": {},
		"embed_colors": {
			"success": "#2ECC71",
			"error": "#ff0000",
			"info": "#3498DB",
		},
	},
	"twitter": {
		"consumer_key": "",
		"consumer_secret": "",
		"access_token": "",
		"access_token_secret": "",
		"queue": [],
	}
}


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
