from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGmPPApFlQX919wPp0scooGKuQFm_tHcBMdp8GGaSX2Oihr5L9&s")
START_IMG = getenv("START_IMG", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHIukuaQi3bjuc4GjT5wfDpcKc00EFW8rPdyXlWbjvrdDb3bvW&s")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ironmanhindigming1")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/irotechlab")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7994776745").split()))


FAILED = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGpDLr8L_l3aqmB0ttPm1fXNtLeuultbIihxD6mLcyu0b9YEfD&s"
