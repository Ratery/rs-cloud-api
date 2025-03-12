from app.dishes.models import Dish
from app.dao.base import BaseDAO


class DishesDAO(BaseDAO):
    model = Dish
