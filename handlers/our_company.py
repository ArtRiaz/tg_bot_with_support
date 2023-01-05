from aiogram import types, Dispatcher
from create_bot import bot, dp
from aiogram.dispatcher.filters import Text
from keyboard.reply import get_back


async def desc(message: types.Message):
    text = 'Адвокаты нашей конторы имеют значительный опыт работы в арбитражных судах и судах общей юрисдикции: в сфере недвижимости, в корпоративных спорах, в спорах с государственными органами и муниципальными образованиями, правовой защите от уголовного, налогового, административного преследования граждан и организаций.'

    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://advokatyufa.ru/wp-content/uploads/2014/09/advokatskaya-kontora.jpg')
    await bot.send_message(chat_id=message.from_user.id, text=text,
                           reply_markup=get_back())




def register_handler_our_company(dp: Dispatcher):
    dp.register_message_handler(desc, Text(equals='О нашей компании'))

