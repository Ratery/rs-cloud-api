from typing import Dict

from fastapi import APIRouter, Response, Depends, HTTPException
from starlette import status

from app.schemas import SResponse, SErrorResponse
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import User
from app.users.schemas import SUserRegister, SUserAuth

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post(
    path='/register/',
    response_model=SResponse[SUserRegister],
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            'description': "Already exists",
            'model': SErrorResponse
        }
    }
)
async def register_user(user_data: SUserRegister) -> SResponse[SUserRegister]:
    user = await UsersDAO.find_one_or_none(username=user_data.username)
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username is already registered"
        )
    user_dict = user_data.model_dump()
    user_dict['password'] = get_password_hash(user_data.password)
    await UsersDAO.add(**user_dict)
    return SResponse(
        success=True,
        message="User registered successfully",
        payload=user_data
    )


@router.post(
    path='/login/',
    response_model=SResponse[Dict[str, str]],
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            'description': "Authentication failed",
            'model': SErrorResponse
        }
    }
)
async def auth_user(response: Response, user_data: SUserAuth) -> SResponse[Dict[str, str]]:
    check = await authenticate_user(username=user_data.username, password=user_data.password)
    if check is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password. Authentication failed.",
        )
    access_token = create_access_token({'sub': str(check.id)})
    response.set_cookie(
        key='access_token',
        value=access_token,
        httponly=True
    )
    return SResponse(
        success=True,
        message="Authentication successful",
        payload={
            'access_token': access_token,
            'refresh_token': ""
        }
    )


@router.post('/logout/')
async def logout_user(response: Response) -> SResponse:
    response.delete_cookie(key='access_token')
    return SResponse(
        success=True,
        message="Logout successful"
    )


@router.get('/me/')
async def get_me(user_data: User = Depends(get_current_user)):
    return user_data
