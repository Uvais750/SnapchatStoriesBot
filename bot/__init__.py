import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID" "37028679"))
    API_HASH = os.environ.get("API_HASH" "898cab6df390b01f50efb6d05b0ca59e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN" "8392704566:AAFJkuZyxV64jHyeQnFro-4RmVPgUQkgkY4")
    BOT_USERNAME = os.environ.get("BOT_USERNAME" "Flash_bgmis_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
