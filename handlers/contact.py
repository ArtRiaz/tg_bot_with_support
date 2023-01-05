from aiogram import types, Dispatcher
from create_bot import bot, dp
from aiogram.dispatcher.filters import Text
from keyboard.inline import ikb_contact


async def cmd_contact(message:types.Message):
    await message.delete()
    await message.answer('Как с нами связаться:',reply_markup=ikb_contact())


def register_handler_contact(dp:Dispatcher):
    dp.register_message_handler(cmd_contact, Text(equals='Контакты'))