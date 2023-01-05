from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from keyboard.inline_support import support_keyboard, support_callback
from aiogram.dispatcher import FSMContext


async def ask_support(message: types.Message):
    text = 'Хотите написать в техподдержку , нажми кнопку ниже👇'
    keyboard = await support_keyboard(messages='one')
    await message.answer(text, reply_markup=keyboard)


async def send_to_support(callback: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await callback.answer()
    user_id = int(callback_data.get('user_id'))

    await callback.message.answer('Пришлите ваше сообщение: ')
    await state.set_state('wait_for_support_message')
    await state.update_data(second_id=user_id)


async def get_support_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    second_id = data.get('second_id')

    await bot.send_message(second_id,
                           f"Вам пришло письмо! Вы можете отправить нажав на кнопку ниже")
    keyboard = await support_keyboard(messages='one', user_id=message.from_user.id)
    await message.copy_to(second_id, reply_markup=keyboard)

    await message.answer('Вы отправили сообщение')
    await state.reset_state()


def get_support(dp: Dispatcher):
    dp.register_message_handler(ask_support, Text('Задать вопрос оператору'))
    dp.register_callback_query_handler(send_to_support, support_callback.filter(messages='one'))
    dp.register_message_handler(get_support_message, state="wait_for_support_message", content_types=types.ContentTypes.ANY)
