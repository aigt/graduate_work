import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT = os.environ.get("STATIC_PATH")

STATIC_URL = "/static/"
