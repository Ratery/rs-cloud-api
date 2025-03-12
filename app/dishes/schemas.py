from typing import List

from pydantic import BaseModel, ConfigDict, Field


class SDishAdd(BaseModel):
    restaurant_id: int = Field(..., description="Restaurant ID")
    name: str = Field(..., min_length=5, max_length=50, description="Dish name")
    description: str = Field(None, description="Dish description")
    weight: int = Field(..., ge=0, description="Dish weight (in grams)")
    fats: int = Field(..., ge=0, description="Fat mass (in grams)")
    carbohydrates: int = Field(..., ge=0, description="Fat mass (in grams)")
    proteins: int = Field(..., ge=0, description="Fat mass (in grams)")
    calories: int = Field(..., ge=0, description="Calories amount")
    composition: List[str] = Field(..., description="Comma-separated list of dish compositions")


class SDish(SDishAdd):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., description="Dish ID")
