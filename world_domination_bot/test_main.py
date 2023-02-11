""""""
import logging
from typing import Dict

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import CallbackQuery
from aiogram.types import Message
from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import Update
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BotBlocked


TOKEN_API = '5912434737:AAEBaVTZLkDZGvZiAhKKTyMUuArkwpDbaJg'
START_COMMAND = """<em>Добро пожаловать в Мировое Господство!</em>"""
HELP_COMMAND = """
/start - начать работу с ботом
/help - список команд
/sticker - получить стикер
/photo - получить фото
/load_photo - загрузить фото
/cancel - отменить диалоговое состояние
"""
COFFEE_STICKER_ID = 'CAACAgQAAxkBAAEHlE5j3W3B6k6Tp6jmXTUgRTDRGFonYQACUAADL9_4Cby5caeHY0FSLgQ'
CAT_PHOTO_URL = 'https://memepedia.ru/wp-content/uploads/2018/07/cover-3-1.jpg'

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


bot = Bot(TOKEN_API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
cb = CallbackData('ikb', 'action')


class GameStatesGroup(StatesGroup):
    """"""
    photo = State()
    desc = State()


async def on_startup(_):
    """"""
    logger.info('Bot was successfully launched')


def get_init_keyboard():
    """"""
    start_button = KeyboardButton('/start')
    help_button = KeyboardButton('/help')
    sticker_button = KeyboardButton('/sticker')
    photo_button = KeyboardButton('/photo')
    load_photo_button = KeyboardButton('/load_photo')

    kb = ReplyKeyboardMarkup(keyboard=[
        [start_button, help_button],
        [sticker_button, photo_button, load_photo_button]],
        resize_keyboard=True)

    return kb


@dp.message_handler(commands=['start'], state=None)
async def start_command(message: Message):
    """"""
    kb = get_init_keyboard()
    await message.answer(START_COMMAND, parse_mode='HTML', reply_markup=kb)
    await message.delete()


def get_cancel_inline_keyboard() -> InlineKeyboardMarkup:
    """"""
    cancel_kb_button = KeyboardButton('/cancel', callback_data=cb.new('cancel'))
    kb = ReplyKeyboardMarkup(keyboard=[
        [cancel_kb_button]])

    return kb


@dp.message_handler(commands=['load_photo'])
async def load_photo_command(message: Message):
    """"""
    await GameStatesGroup.photo.set()
    cancel_kb = get_cancel_inline_keyboard()
    await message.answer('Отправь фотографию!',
                         reply_markup=cancel_kb)
    await message.delete()


@dp.message_handler(commands=['cancel'], state='*')
async def cancel_command(message: Message, state: FSMContext):
    """"""
    kb = get_init_keyboard()
    await message.reply('Состояние сброшено', reply_markup=kb)
    await state.finish()


@dp.message_handler(commands=['photo'])
async def photo_command(message: Message):
    """"""
    ikb = get_vote_inline_keyboard()
    await bot.send_photo(
        message.from_user.id, photo=CAT_PHOTO_URL, caption='Нравится?', reply_markup=ikb)
    await message.delete()


@dp.message_handler(lambda message: not message.photo, state=GameStatesGroup.photo)
async def validate_photo(message: Message):
    """"""
    await message.reply('Это не фотография!')


@dp.message_handler(lambda message: message.photo,
                    content_types=['photo'],
                    state=GameStatesGroup.photo)
async def load_photo(message: Message, state: FSMContext):
    """"""
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await GameStatesGroup.next()
    await message.reply('А теперь отправь описание!')


@dp.message_handler(state=GameStatesGroup.desc)
async def load_desc(message: Message, state: FSMContext):
    """"""
    logger.info('checking desc')
    async with state.proxy() as data:
        data['desc'] = message.text
    await message.reply('Фото сохранено!')

    kb = get_init_keyboard()
    async with state.proxy() as data:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=data['desc'],
                             reply_markup=kb)

    await state.finish()


@dp.message_handler(commands=['help'])
async def help_command(message: Message):
    """"""
    await message.reply(HELP_COMMAND)
    await message.delete()


@dp.message_handler(commands=['sticker'])
async def sticker_command(message: Message):
    """"""
    await bot.send_sticker(message.from_user.id, sticker=COFFEE_STICKER_ID)
    await message.delete()


def get_vote_inline_keyboard() -> InlineKeyboardMarkup:
    """"""
    like_ikb_button = InlineKeyboardButton(text='❤', callback_data=cb.new('like'))
    dislike_ikb_button = InlineKeyboardButton(text='💔', callback_data=cb.new('dislike'))
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [like_ikb_button, dislike_ikb_button]],
        row_width=2)

    return ikb


@dp.message_handler()
async def reply_with_emoji(message: Message):
    """"""
    await message.reply(f'{message.text} 🤣')


@dp.callback_query_handler(cb.filter())
async def vote_callback(callback: CallbackQuery, callback_data: Dict):
    if callback_data['action'] == 'like':
        await callback.answer(text='Ура!')
    elif callback_data['action'] == 'dislike':
        await callback.answer(text='Ну и ладно!')
    else:
        raise ValueError('{callback.data} callback data value is not supported.')


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked_handler(update: Update, exception: BotBlocked) -> bool:
    """"""
    logger.error('Нельзя отправить сообщение, потому что бота заблокировали.')
    return True


def main():
    """"""
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import traceback
        logger.warning(traceback.format_exc())
    finally:
        pass
