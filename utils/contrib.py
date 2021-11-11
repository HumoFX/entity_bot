from aiogram import types

from utils.db.models import User


async def get_user(user_id=None):
    """Returns user object"""
    user = User.get(user_id)
    return user
