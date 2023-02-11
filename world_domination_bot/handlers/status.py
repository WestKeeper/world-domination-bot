from aiogram.types import Message
from sqlalchemy.orm import Session

from db.services.countries import get_countries
from db.session import get_db
from keyboards.default.init_keyboard import get_init_keyboard
from templates.templates import render_template


async def status_command(message: Message, db: Session = next(get_db())):
    """"""
    kb = get_init_keyboard()
    countries = get_countries(db)
    for country in countries:
        await message.answer(
            render_template('countries/country.j2',
                            {'country': country}),
            parse_mode='HTML', reply_markup=kb
        )
    await message.delete()
