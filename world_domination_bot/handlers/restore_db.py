from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from sqlalchemy.orm import Session

from common.config import TEST_MODE
from common.config import TO_GENERATE_AND_DROP_DB
# from common.fake_data_generation_lib import generate_test_session
from db.db_lib import create_tables
from db.db_lib import drop_tables
# from db.services.leaders import update_leader_by_name
from db.session import get_db
from keyboards.default.round_keyboard import get_round_keyboard
from templates.templates import render_template


async def restore_db_command(message: Message, state: FSMContext, db: Session = next(get_db())):
    """"""
    kb = get_round_keyboard()
    if TO_GENERATE_AND_DROP_DB:
        drop_tables()
        create_tables()
        generate_test_session(db)
        if TEST_MODE:
            update_leader_by_name('Си Цзиньпин', db, user_id=message.from_user.id)

    await state.finish()
    await message.answer(render_template('db/restore_db.j2'), parse_mode='HTML', reply_markup=kb)
    await message.delete()
