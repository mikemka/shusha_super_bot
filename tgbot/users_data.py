from config import USERS_JSON_PATH
import simplejson as json


def load_users_json() -> dict:
    with open(USERS_JSON_PATH) as json_file:
        return json.load(json_file)


def dump_users_json(json_serializeable: dict) -> None:
    with open(USERS_JSON_PATH, 'w') as json_file:
        return json.dump(json_serializeable, json_file)


def generate_main_text(users_info: dict, user_id: int) -> str:
    return (
        '<b>Привет! Этот бот поможет тебе выбрать самый оптимальный маршрут на поезде и электричке!</b>\n\n'
        f'<i>Отправление</i>: {users_info[str(user_id)]["start"] if users_info[str(user_id)]["start"] else "-"}\n'
        f'<i>Прибытие</i>: {users_info[str(user_id)]["stop"] if users_info[str(user_id)]["stop"] else "-"}\n'
        'Для смены значений нажмите на соответствующую кнопку. Для поиска маршрута введите /search'
    )