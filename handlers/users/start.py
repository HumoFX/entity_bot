from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message,  state: FSMContext):
    await state.reset_state()  # Обнуляет Машину
    user = await get_user()
    if not user:
        await message.answer(TXT['choose_language'], reply_markup=start_language_buttons())
        await RegistrationState.language.set()
    else:
        # If user comes again activate status
        await activate_user(message.from_user.id)
        await message.answer(_(TXT['welcome']), reply_markup=user_main_menu())
