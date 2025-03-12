from app.restaurants.models import Restaurant
from app.dao.base import BaseDAO


class RestaurantsDAO(BaseDAO):
    model = Restaurant
