from aiogram.types import Message
from sqlalchemy.orm import Session

from db.services.countries import get_countries_with_leaders
from db.session import get_db
from templates.templates import render_template


async def status_command(message: Message, db: Session = next(get_db())):
    """"""
    countries = get_countries_with_leaders(db)
    for country in countries:
        await message.answer(
            render_template('countries/country.j2',
                            {'country': country,
                             'is_user_country': country.user_id == message.from_user.id}),
            parse_mode='HTML',
        )
    await message.delete()
