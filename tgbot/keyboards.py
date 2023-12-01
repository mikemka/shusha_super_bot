from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
# from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


def generate_main_keyboard(train=True):
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            text='Отправление',
            callback_data='start',
        ),
        InlineKeyboardButton(
            text='Прибытие',
            callback_data='stop',
        ),
    ).add(
        InlineKeyboardButton(
            text='Очистить',
            callback_data='delete'
        )
    )

BACK_BTN_KEYBOARD = InlineKeyboardMarkup().add(
    InlineKeyboardButton(
        text='Назад',
        callback_data='back',
    ),
)
