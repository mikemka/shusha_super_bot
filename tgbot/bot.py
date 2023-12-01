import logging
from aiogram import executor
from dispather import dp
import handlers


logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    handlers
    
    executor.start_polling(dp, skip_updates=True)
