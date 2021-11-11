from aiogram.contrib.middlewares.i18n import I18nMiddleware
from data.config import I18N_DOMAIN, LOCALES_DIR
from utils.db_api.user_commands import get_user_lang

from aiogram.types import ChatType, Chat


class ACLMiddleware(I18nMiddleware):
    # Каждый раз, когда нужно узнать язык пользователя - выполняется эта функция
    async def get_user_locale(self, action, args):
        chat = Chat.get_current()

        if chat and chat.type == ChatType.PRIVATE:
            user_lang = await get_user_lang()

            return user_lang or 'ru'


def setup_middleware(dp):
    # Устанавливаем миддлварь
    i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
    dp.middleware.setup(i18n)
    return i18n
