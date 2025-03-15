import json
import asyncio

from app.restaurants.dao import RestaurantsDAO
from app.dishes.dao import DishesDAO


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


async def main():
    restaurants_data = load_data('app/init_db/restaurants.json')
    await RestaurantsDAO.add_many(restaurants_data)

    dishes_data = load_data('app/init_db/dishes.json')
    await DishesDAO.add_many(dishes_data)


if __name__ == '__main__':
    asyncio.run(main())
