from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from data import config
# from middlewares.language_middleware import setup_middleware

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML, proxy=config.HTTP_PROXY)
storage = RedisStorage2('localhost', 6379, db=5, pool_size=10, prefix='my_fsm_key')
dp = Dispatcher(bot, storage=storage)


# Настроим i18n middleware для работы с многоязычностью
# i18n = setup_middleware(dp)
# _ = i18n.gettext
