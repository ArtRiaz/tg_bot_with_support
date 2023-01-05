from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def kb_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[
        KeyboardButton('Меню')
    ]])

    return kb

def get_kb_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton('О нашей компании'), KeyboardButton('Наша Команда')
    ],[
        KeyboardButton('Запись на консультацию'), KeyboardButton('Задать вопрос оператору')
    ],[
        KeyboardButton('Контакты'), KeyboardButton('Онлайн консультация')
    ]

    ])

    return kb

def get_back():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton('👈 Назад в главное меню')
    ]])

    return kb
