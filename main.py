from aiogram import executor, types
import db_sqlite
from db_sqlite import *
from create_bot import dp
from middleware.support_middleware import SupportMiddleware
from handlers import start, our_company, back_to_menu, profiles, contact, inline_menu, registration, support, \
    support_call
from aiogram.dispatcher import middlewares


async def on_startup(_):
    db_sqlite.sq.connect('database.db')
    print('Бот запущен')
    print('База данных запущена')


dp.middleware.setup(SupportMiddleware())

start.register_handlers_start(dp)
our_company.register_handler_our_company(dp)
back_to_menu.register_handler_back(dp)
profiles.register_handler_profiles(dp)
contact.register_handler_contact(dp)
inline_menu.register_inline_menu(dp)
registration.consultat(dp)
support.get_support(dp)
support_call.get_support_call(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)
