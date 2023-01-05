from aiogram import types, Dispatcher
from create_bot import dp, storage
from aiogram.dispatcher.filters import Text
from state import ClientStateGroup
from aiogram.dispatcher import FSMContext
from keyboard.reply import get_back
from db_sqlite import create_profiles, edit_profile


async def registr_consultat(message: types.Message):
    await create_profiles(user_id=message.from_user.id)
    await message.delete()
    await message.answer('Для того, чтобы зарегистривоваться к нам на консультацию, '
                         'пройди регистрацию.В ближайшее время наш секретарь свяжеться с Вами.')
    await message.answer(' Введите свое имя:')
    await ClientStateGroup.name.set()


async def add_name(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.istitle():
        async with state.proxy() as data:
            data['name'] = answer
        # await state.update_data(name=answer)
        await message.answer('Введите свою фамилию:')

        await ClientStateGroup.surname.set()
    else:
        await message.answer('Введите имя корректно и с большой буквы')


async def add_surname(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.istitle():
        async with state.proxy() as data:
            data['surname'] = answer
        # await state.update_data(surname=answer)
        await message.answer('Введите свой контактный номер телефона:')

        await ClientStateGroup.phone.set()
    else:
        await message.answer('Введите фамилию корректно и с большой буквы')


async def add_phone(message: types.Message, state: FSMContext):
    answer = message.text

    if answer.replace('+', '').isnumeric():
        async with state.proxy() as data:
            data['phone'] = answer
        #  await state.update_data(phone=answer)
        await message.answer('Введите свой e-mail:')
        await ClientStateGroup.email.set()
    else:
        await message.answer('Введите корректный номер:')


async def add_email(message: types.Message, state: FSMContext):
    answer = message.text
    if '@' in answer:
        async with state.proxy() as data:
            data['email'] = answer
        # await state.update_data(email=answer)
        data = await state.get_data()
        name = data.get('name')
        surname = data.get('surname')
        phone = data.get('phone')
        email = data.get('email')
        await edit_profile(state, user_id=message.from_user.id)
        await message.answer(f'Ваша регистрация успешно выполнина.\n'
                             f'Вас зовут: {name}\n'
                             f'Ваша фамилия: {surname}\n'
                             f'Ваш номер телефона: {phone}\n'
                             f'Ваш e-mail: {email}',
                             reply_markup=get_back())

        await ClientStateGroup.email.set()
        await state.finish()
    else:
        await message.answer('Введите корректный e-mail:')


def consultat(dp: Dispatcher):
    dp.register_message_handler(registr_consultat, Text(equals='Запись на консультацию'))
    dp.register_message_handler(add_name, state=ClientStateGroup.name)
    dp.register_message_handler(add_surname, state=ClientStateGroup.surname)
    dp.register_message_handler(add_phone, state=ClientStateGroup.phone)
    dp.register_message_handler(add_email, state=ClientStateGroup.email)
