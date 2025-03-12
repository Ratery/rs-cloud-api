from typing import List

from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, HTTPException, status

from app.dishes.models import Dish
from app.dishes.schemas import SDish, SDishAdd
from app.dishes.dao import DishesDAO
from app.schemas import SResponse, SErrorResponse

router = APIRouter(prefix='/dishes', tags=['Dishes'])


@router.get(
    path='/',
    response_model=SResponse[List[SDish]]
)
async def get_all() -> SResponse[List[SDish]]:
    all_dishes = await DishesDAO.find_all()
    return SResponse(
        success=True,
        message="Success",
        payload=[dish.to_dict() for dish in all_dishes]
    )


@router.get(
    path='/{dish_id}',
    response_model=SResponse[SDish],
    responses={
        status.HTTP_404_NOT_FOUND: {
            'description': "Dish not found",
            'model': SErrorResponse
        }
    }
)
async def get_dish_by_id(dish_id: int) -> SResponse[SDish]:
    dish = await DishesDAO.find_one_or_none_by_id(dish_id)
    if dish is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dish with the provided ID not found"
        )
    return SResponse(
        success=True,
        message="Success",
        payload=dish.to_dict()
    )


@router.post(
    path='/add/',
    status_code=status.HTTP_201_CREATED,
    response_model=SResponse[SDish],
    responses={
        status.HTTP_404_NOT_FOUND: {
            'description': "Restaurant not found",
            'model': SErrorResponse
        }
    }
)
async def add_dish(dish: SDishAdd) -> SResponse[SDish]:
    try:
        dish: Dish = await DishesDAO.add(**dish.model_dump())
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Restaurant with the provided ID not found"
        )
    return SResponse(
        success=True,
        message="Dish added successfully",
        payload=dish.to_dict()
    )


@router.delete(
    path='/delete/{dish_id}',
    response_model=SResponse,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'description': "Dish not found",
            'model': SErrorResponse
        }
    }
)
async def delete_dish_by_id(dish_id: int) -> SResponse:
    deleted = await DishesDAO.delete(id=dish_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dish with the provided ID not found"
        )
    return SResponse(
        success=True,
        message="Dish deleted successfully"
    )
