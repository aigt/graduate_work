from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

include(
    "components/auth.py",
    "components/base_dir.py",
    "components/database.py",
    "components/debug.py",
    "components/installed_apps.py",
    "components/internationalization.py",
    "components/middleware.py",
    "components/network.py",
    "components/secrets.py",
    "components/templates.py",
)
