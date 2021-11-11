import asyncio
import os

from aiogram import executor

import handlers
from loader import dp
from utils.db.connect import async_db_session
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def init_app():
    await async_db_session.init()
    await async_db_session.create_all()


async def on_startup(dispatcher):
    # middlewares
    # filters
    handlers
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    await init_app()
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


async def on_shutdown(dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    if os.name == "nt":  # Windows
        policy = asyncio.WindowsSelectorEventLoopPolicy()
        asyncio.set_event_loop_policy(policy)
    executor.start_polling(dp, on_startup=on_startup)
