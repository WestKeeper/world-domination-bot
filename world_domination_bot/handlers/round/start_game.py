import random

from aiogram import Bot
from aiogram.types import Message
from sqlalchemy.orm import Session

from db.services.cities import get_country_cities
from db.services.countries import get_all_countries
from db.services.game_sessions import activate_game_session_by_session_id
from db.services.game_sessions import get_session_by_host_user_id
from db.services.game_sessions import get_session_users
from db.services.leaders import create_leader
from db.services.leaders import get_leader_by_user_id_n_session_id
from db.services.rounds import activate_round
from db.services.rounds import get_active_round
from db.services.session_cities import create_session_city
from db.services.session_countries import create_session_country
from db.services.session_countries import get_session_country_by_leader_id
from db.session import get_db
from keyboards.default.round_keyboard import get_round_keyboard
from states.game_states_group import GameStatesGroup
from templates.templates import render_template


async def start_game_command(message: Message, db: Session = next(get_db())):
    """"""
    session = get_session_by_host_user_id(host_user_id=message.from_user.id, db=db)

    users = get_session_users(session_id=session.id, db=db)
    countries = get_all_countries(db=db)
    chosen_countries = random.sample(countries, len(users))

    bot = Bot.get_current()
    user_country_dict = {}
    for user, chosen_country in zip(users, chosen_countries):
        create_leader(user.user_id, session.id, db=db)
        leader = get_leader_by_user_id_n_session_id(user.user_id, session.id, db=db)
        create_session_country(
            budget=chosen_country.init_budget,
            has_nuke_tech=False,
            bombs_number=0,
            country_name=chosen_country.name,
            leader_id=leader.id,
            db=db,
        )
        session_country = get_session_country_by_leader_id(leader_id=leader.id, db=db)
        cities = get_country_cities(country_name=chosen_country.name, db=db)
        for city in cities:
            create_session_city(
                has_shield=city.init_has_shield,
                development=city.init_development,
                development_number=0,
                life_level=city.init_life_level,
                is_alive=True,
                city_name=city.name,
                session_country_id=session_country.id,
                db=db,
            )

        user_country_dict[user.name] = chosen_country.name

    activate_game_session_by_session_id(session.id, db=db)

    for user in users:
        await bot.send_message(user.user_id,
                               render_template('rounds/game_started.j2',
                                               {'session': session,
                                                'user': user,
                                                'user_country_dict': user_country_dict}),
                                                parse_mode='HTML')

    activate_round(number=1, session_id=session.id, db=db)
    round = get_active_round(session_id=session.id, db=db)

    kb = get_round_keyboard()
    await GameStatesGroup.round.set()
    for user in users:
        await bot.send_message(user.user_id,
                               render_template('rounds/round_started.j2',
                                               {'session': session,
                                               'round': round}),
                                               parse_mode='HTML', reply_markup=kb)
    await message.delete()
