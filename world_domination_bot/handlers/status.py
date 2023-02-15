from aiogram.types import Message
from sqlalchemy.orm import Session

from common.order_lib.calculate_mean_life_level import calculate_mean_life_level
from db.services.countries import get_countries_with_leaders
from db.services.game_sessions import get_session_by_user_id
from db.session import get_db
from templates.templates import render_template


async def status_command(message: Message, db: Session = next(get_db())):
    """"""
    session = get_session_by_user_id(user_id=message.from_user.id, db=db)
    await message.answer(
        render_template('game_sessions/session.j2', {'session': session}), parse_mode='HTML')

    countries = get_countries_with_leaders(db)
    for country in countries:
        mean_life_level = calculate_mean_life_level(cities=country.cities)
        await message.answer(
            render_template('countries/country.j2',
                            {'country': country,
                             'is_user_country': country.user_id == message.from_user.id,
                             'mean_life_level': round(mean_life_level, 2)}),
            parse_mode='HTML',
        )
    await message.delete()
