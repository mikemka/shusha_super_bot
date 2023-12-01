from aiogram import types
from aiogram.dispatcher.filters import Text
from dispather import dp
from keyboards import BACK_BTN_KEYBOARD, generate_main_keyboard
from users_data import load_users_json, dump_users_json, generate_main_text


@dp.callback_query_handler(Text(equals='start'))
async def help_callback(callback: types.CallbackQuery):
    users_info = load_users_json()
    users_info[str(callback.from_user.id)]['wait'] = 'start'
    dump_users_json(users_info)

    await callback.message.edit_text(
        text='Напишите точку своего отправления, или нажмите "Назад"',
        reply_markup=BACK_BTN_KEYBOARD,
    )
    await callback.answer()


@dp.callback_query_handler(Text(equals='stop'))
async def help_callback(callback: types.CallbackQuery):
    users_info = load_users_json()
    users_info[str(callback.from_user.id)]['wait'] = 'stop'
    dump_users_json(users_info)

    await callback.message.edit_text(
        text='Напишите точку своего прибытия, или нажмите "Назад"',
        reply_markup=BACK_BTN_KEYBOARD,
    )
    await callback.answer()


@dp.callback_query_handler(Text(equals='delete'))
async def help_callback(callback: types.CallbackQuery):
    users_info = load_users_json()
    x = users_info[str(callback.from_user.id)]
    if x['start'] is None and x['stop'] is None and x['day'] is None:
        return await callback.answer('Информация не может быть удалена!')
    users_info[str(callback.from_user.id)]['start'] = None
    users_info[str(callback.from_user.id)]['stop'] = None
    users_info[str(callback.from_user.id)]['day'] = None
    users_info[str(callback.from_user.id)]['wait'] = None
    dump_users_json(users_info)
    await callback.message.edit_text(
        text=generate_main_text(load_users_json(), callback.from_user.id),
        reply_markup=generate_main_keyboard(users_info[str(callback.from_user.id)]['train']),
    )
    await callback.answer()


@dp.callback_query_handler(Text(equals='type'))
async def help_callback(callback: types.CallbackQuery):
    users_info = load_users_json()
    users_info[str(callback.from_user.id)]['train'] = not users_info[str(callback.from_user.id)]['train']
    dump_users_json(users_info)
    await callback.message.edit_text(
        text=generate_main_text(load_users_json(), callback.from_user.id),
        reply_markup=generate_main_keyboard(users_info[str(callback.from_user.id)]['train']),
    )
    await callback.answer()


@dp.callback_query_handler(Text(equals='back'))
async def help_callback(callback: types.CallbackQuery):
    users_info = load_users_json()
    users_info[str(callback.from_user.id)]['wait'] = None
    dump_users_json(users_info)
    await callback.message.edit_text(
        text=generate_main_text(users_info, callback.from_user.id),
        reply_markup=generate_main_keyboard(users_info[str(callback.from_user.id)]['train']),
    )
    await callback.answer()
