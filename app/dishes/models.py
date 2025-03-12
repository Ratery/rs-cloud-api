from sqlalchemy import Text, ARRAY, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base, int_pk


class Dish(Base):
    __tablename__ = "dishes"

    id: Mapped[int_pk]
    restaurant_id: Mapped[int] = mapped_column(ForeignKey('restaurants.id'), nullable=False)
    restaurant: Mapped['Restaurant'] = relationship(back_populates='dishes')

    name: Mapped[str]
    description: Mapped[str] = mapped_column(Text, nullable=True)
    weight: Mapped[int]
    fats: Mapped[int]
    carbohydrates: Mapped[int]
    proteins: Mapped[int]
    calories: Mapped[int]
    composition: Mapped[ARRAY[String]] = mapped_column(ARRAY(String))

    extend_existing = True

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"

    def to_dict(self):
        return {
            'id': self.id,
            'restaurant_id': self.restaurant_id,
            'name': self.name,
            'description': self.description,
            'weight': self.weight,
            'fats': self.fats,
            'carbohydrates': self.carbohydrates,
            'proteins': self.proteins,
            'calories': self.calories,
            'composition': self.composition
        }
