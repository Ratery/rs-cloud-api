from typing import List

from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError

from app.dishes.schemas import SDish
from app.restaurants.models import Restaurant
from app.restaurants.schemas import SRestaurant, SRestaurantAdd
from app.restaurants.dao import RestaurantsDAO
from app.schemas import SResponse, SErrorResponse

router = APIRouter(prefix='/restaurants', tags=['Restaurants'])


@router.get(
    path='/',
    response_model=SResponse[List[SRestaurant]]
)
async def get_all() -> SResponse[List[SRestaurant]]:
    all_restaurants = await RestaurantsDAO.find_all()
    return SResponse(
        success=True,
        message="Success",
        payload=[restaurant.to_dict() for restaurant in all_restaurants]
    )


@router.get(
    path='/{restaurant_id}',
    response_model=SResponse[SRestaurant],
    responses={
        status.HTTP_404_NOT_FOUND: {
            'description': "Restaurant not found",
            'model': SErrorResponse
        }
    }
)
async def get_restaurant_by_id(restaurant_id: int) -> SResponse[SRestaurant]:
    restaurant = await RestaurantsDAO.find_one_or_none_by_id(restaurant_id)
    if restaurant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Restaurant with the provided ID not found"
        )
    return SResponse(
        success=True,
        message="Success",
        payload=restaurant.to_dict()
    )


@router.get(
    path='/{restaurant_id}/menu',
    response_model=SResponse[List[SDish]],
    responses={
        status.HTTP_404_NOT_FOUND: {
            'description': "Restaurant not found",
            'model': SErrorResponse
        }
    }
)
async def get_restaurant_menu_by_id(restaurant_id: int) -> SResponse[List[SDish]]:
    restaurant = await RestaurantsDAO.find_one_or_none_by_id(restaurant_id)
    if restaurant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Restaurant with the provided ID not found"
        )
    return SResponse(
        success=True,
        message="Success",
        payload=[dish.to_dict() for dish in restaurant.dishes]
    )


@router.post(
    path='/add/',
    status_code=status.HTTP_201_CREATED,
    response_model=SResponse[SRestaurant],
    responses={
        status.HTTP_409_CONFLICT: {
            'description': "Already exists",
            'model': SErrorResponse
        }
    }
)
async def add_restaurant(dish: SRestaurantAdd) -> SResponse[SRestaurant]:
    try:
        restaurant: Restaurant = await RestaurantsDAO.add(**dish.model_dump())
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Restaurant with the provided name is already exists"
        )
    return SResponse(
        success=True,
        message="Restaurant added successfully",
        payload=restaurant.to_dict()
    )


@router.delete(
    path='/delete/{restaurant_id}',
    response_model=SResponse[SRestaurant],
    responses={
        status.HTTP_404_NOT_FOUND: {
            'description': "Restaurant not found",
            'model': SErrorResponse
        }
    }
)
async def delete_restaurant_by_id(restaurant_id: int) -> SResponse[SRestaurant]:
    deleted = await RestaurantsDAO.delete(id=restaurant_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Restaurant with the provided ID not found"
        )
    return SResponse(
        success=True,
        message="Restaurant deleted successfully"
    )
