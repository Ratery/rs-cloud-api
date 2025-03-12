from starlette.exceptions import HTTPException

from fastapi import Request
from fastapi.responses import JSONResponse

from app.schemas import SErrorResponse


async def exception_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content=SErrorResponse(
            success=False,
            message=str(exc)
        ).model_dump()
    )


async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content=SErrorResponse(
            success=False,
            message=exc.detail
        ).model_dump()
    )
