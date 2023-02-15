""""""
import logging
from logging import Logger
import os
from pathlib import Path
import sys

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage


ROOT_DIR = Path(os.getcwd()).resolve()
if ROOT_DIR not in sys.path:
    sys.path.append(str(ROOT_DIR))


from common.config import TO_GENERATE_AND_DROP_DB
from common.config import TOKEN_API
from common.fake_data_generation_lib import generate_test_session
from common.logger import setup_logging
from db.db_lib import create_tables
from db.db_lib import drop_tables
from db.models.game_sessions import GameSession
from db.session import get_db
from handlers.handlers import register_handlers


async def on_startup(_, db: GameSession = next(get_db())):
    """"""
    logger.info('Bot was successfully launched')
    if TO_GENERATE_AND_DROP_DB:
        generate_test_session(db)
    logger.info('Test data was generated successfully.')


async def on_shutdown(dp: Dispatcher, db: GameSession = next(get_db())):
    logging.warning('Shutting down..')
    if TO_GENERATE_AND_DROP_DB:
        drop_tables()
    await dp.storage.close()
    await dp.storage.wait_closed()
    await dp.bot.session.close()
    logging.warning('Bye!')


def main(logger: Logger):
    """"""
    create_tables()

    bot = Bot(TOKEN_API)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    register_handlers(dp)

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)


if __name__ == '__main__':
    logger = setup_logging()
    try:
        main(logger)
    except Exception:
        import traceback
        logger.error(traceback.format_exc())
    finally:
        pass
