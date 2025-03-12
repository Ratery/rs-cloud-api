from typing import List

from pydantic import BaseModel, ConfigDict, Field


class SRestaurantAdd(BaseModel):
    name: str = Field(..., min_length=5, max_length=50, description="Restaurant unique name")
    description: str = Field(None, description="Restaurant description")
    location: str = Field(..., description="Restaurant address")


class SRestaurant(SRestaurantAdd):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., description="Restaurant ID")
    dishes_ids: List[int] = Field(..., description="Restaurant dishes")
