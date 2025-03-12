from starlette.exceptions import HTTPException
from fastapi import FastAPI

from app.exceptions import exception_handler, http_exception_handler
from app.users.router import router as router_users
from app.dishes.router import router as router_dishes
from app.restaurants.router import router as router_restaurants

app = FastAPI(
    exception_handlers={
        Exception: exception_handler,
        HTTPException: http_exception_handler
    }
)


@app.get("/")
async def root():
    ...

app.add_exception_handler(Exception, exception_handler)

app.include_router(router_users)

app.include_router(router_dishes)

app.include_router(router_restaurants)
