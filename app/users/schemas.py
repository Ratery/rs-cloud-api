from pydantic import BaseModel, Field


class SUserRegister(BaseModel):
    password: str = Field(..., min_length=5, max_length=50, description="Password, from 5 to 50 symbols")
    username: str = Field(..., min_length=3, max_length=50, description="Username, 5 to 50 symbols")
    first_name: str = Field(..., min_length=3, max_length=50, description="First name, from 2 to 30 symbols")
    last_name: str = Field(..., min_length=3, max_length=30, description="Last name, from 3 to 30 symbols")


class SUserAuth(BaseModel):
    username: str = Field(..., min_length=5, max_length=50, description="Username, from 5 to 50 symbols")
    password: str = Field(..., min_length=5, max_length=50, description="Password, from 5 to 50 symbols")
