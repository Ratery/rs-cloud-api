import json
import asyncio

from alembic import command
from alembic.config import Config

from app.restaurants.dao import RestaurantsDAO
from app.dishes.dao import DishesDAO


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


async def add_data():
    restaurants_data = load_data('app/init_db/restaurants.json')
    await RestaurantsDAO.add_many(restaurants_data)

    dishes_data = load_data('app/init_db/dishes.json')
    await DishesDAO.add_many(dishes_data)


def run_migrations():
    alembic_config = Config('alembic.ini')
    command.upgrade(alembic_config, 'head')


if __name__ == '__main__':
    run_migrations()
    asyncio.run(add_data())
