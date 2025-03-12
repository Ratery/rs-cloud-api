from typing import List

from sqlalchemy.orm import Mapped, relationship

from app.database import Base, int_pk, str_uniq, str_nullable


class Restaurant(Base):
    id: Mapped[int_pk]
    name: Mapped[str_uniq]
    description: Mapped[str_nullable]
    location: Mapped[str]
    dishes: Mapped[List['Dish']] = relationship(
        back_populates='restaurant',
        lazy='selectin',
        cascade='all, delete-orphan'
    )

    extend_existing = True

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'dishes_ids': [dish.id for dish in self.dishes]
        }
