import logging
from typing import Any

from utils import misc as misc

DEBUG_MODE = True
# DEBUG_MODE = False

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Always set this high to allow all messages

# Set up handler and formatter
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# Attach the handler only if DEBUG_MODE is True
if DEBUG_MODE:
    logger.addHandler(handler)


def debug_message(msg: Any, lvl: int) -> None:
    logger.log(lvl, msg)
