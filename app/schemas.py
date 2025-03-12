from typing import Generic, TypeVar, Optional

from pydantic import BaseModel

T = TypeVar('T')


class SResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str
    payload: Optional[T] = None


class SErrorResponse(BaseModel):
    success: bool = False
    message: str
