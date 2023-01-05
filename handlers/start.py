from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboard.reply import kb_menu, get_kb_menu
from aiogram.dispatcher.filters import Text



async def cmd_start(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://www.facebook.com/saverne.fc/photos/a.107939831959921/151105374310033/',
                         caption=f'Добро пожаловать {message.from_user.full_name} в нашу компанию!\n'
                                 f'Нажмите кнопку меню, чтоб узнать о нас подробнее👇'
                         , reply_markup=kb_menu())


async def cmd_menu(message: types.Message):
    await message.answer('Управления меню', reply_markup=get_kb_menu())


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(cmd_menu, Text(equals='Меню'))
