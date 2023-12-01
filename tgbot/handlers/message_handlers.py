from aiogram import types
from config import ROUTES_PATH
from dispather import dp
from keyboards import generate_main_keyboard
from users_data import load_users_json, dump_users_json, generate_main_text
from requests import get
import csv


@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message) -> None:
    users_info = load_users_json()
    if str(message.from_user.id) not in users_info:
        users_info[str(message.from_user.id)] = {
            'start': None,
            'stop': None,
            'day': None,
            'train': False,
            'wait': None,
        }
        dump_users_json(users_info)
    await message.answer(
        text=generate_main_text(users_info, message.from_user.id),
        reply_markup=generate_main_keyboard(users_info[str(message.from_user.id)]['train']),
    )


@dp.message_handler(commands='search')
async def search_message(message: types.Message) -> None:
    users_info = load_users_json()
    z = []
    with open(ROUTES_PATH, 'r') as asdmfl:
        x = csv.reader(asdmfl, delimiter=';')
        for y in x:
            z += [y]
    z1 = False
    for i in z:
        if users_info[str(message.from_user.id)]['start'].lower() in i[1].lower() and users_info[str(message.from_user.id)]['stop'].lower() in i[3].lower():
            x1 = i[1]
            x2 = i[3]
            z1 = True
            z = i
            break
    if not z1:
        return await message.answer('Нет такого маршрута!')
    url = (
        f'https://suggest.travelpayouts.com/search?service=tutu_trains&term={z[0]}&term2={z[2]}'
    )
    data = get(url).json()
    if not data:
        return await message.answer('Сегодня уехать не получится!')

    out_url = 'https://www.tutu.ru' + data['url']
    info = {
        'coupe': 'купе', 'lux': 'люкс', 'platskart': 'плацкарт'
    }
    await message.answer(
        f'<a href="{out_url}">{x1} -> {x2}</a>\n\n'
        f'Время отправления: {data["trips"][0]["departureTime"][:-3]}\n'
        f'Время прибытия: {data["trips"][0]["arrivalTime"][:-3]}\n\n'
        f'Цена поездки: {data["trips"][0]["categories"][0]["price"]} руб.\n'
        f'Тип поездки: {info.get(data["trips"][0]["categories"][0]["type"], data["trips"][0]["categories"][0]["type"])}'
    )


@dp.message_handler()
async def get_data_message(message: types.Message) -> None:
    users_info = load_users_json()
    match users_info[str(message.from_user.id)]['wait']:
        case None:
            return await message.delete()
        case 'start':
            users_info[str(message.from_user.id)]['start'] = message.text
        case 'stop':
            users_info[str(message.from_user.id)]['stop'] = message.text
        case 'day':
            users_info[str(message.from_user.id)]['day'] = message.text
    dump_users_json(users_info)
    await message.answer(
        text=generate_main_text(users_info, message.from_user.id),
        reply_markup=generate_main_keyboard(users_info[str(message.from_user.id)]['train']),
    )
