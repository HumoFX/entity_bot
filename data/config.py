from pathlib import Path

from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

PG_USER = env.str("PG_USER")
PG_PASSWORD = env.str("PG_PASSWORD")
DATABASE = env.str("DATABASE")

ADMIN_ID = env.str("ADMIN_ID")
API_TOKEN = env.str("API_TOKEN")
HTTP_PROXY = env.str("HTTP_PROXY")

# LOGS_CHANNEL = -1001175006114
LOGS_CHANNEL = -1001644884708

# Ссылка подключения к базе данных
POSTGRES_URI = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{IP}/{DATABASE}"

I18N_DOMAIN = 'entity_bot'
BASE_DIR = Path(__file__).parent.parent
LOCALES_DIR = BASE_DIR / 'locales'
