from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def ikb_contact():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('Наш сайт',
                             url='https://www.google.com')
    ],[InlineKeyboardButton('Инстаграм', url='https://www.instagram.com/artemriazantsev22/')],[
        InlineKeyboardButton('Геолокация', callback_data='Геолокация')
    ],[
        InlineKeyboardButton('Вызов',callback_data='Вызов')
    ]])

    return ikb

