import asyncio
from aiogram import types, Dispatcher
from create_bot import bot,dp
from aiogram.dispatcher.filters import Text
from keyboard.reply import get_back

async def all_profiles(message:types.Message):

    photo='https://vsegda-pomnim.com/pustyni/11035-pustoe-lico-60-foto.html'
    text = "ГРИГОРИЙ ИВАНОВ \n Оказание помощи юридическим лицам.Составления заявлений, исков, жалоб, ходотайств, договоров."

    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo,
                         caption=text)
    await asyncio.sleep(3)
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo,
                         caption=text)
    await asyncio.sleep(3)
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo,
                         caption=text)
    await asyncio.sleep(3)
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo,
                         caption=text,reply_markup=get_back())
def register_handler_profiles(dp: Dispatcher):
    dp.register_message_handler(all_profiles, Text(equals='Наша Команда') )