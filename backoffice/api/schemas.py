from uuid import UUID
from typing import Optional, Union, List

from pydantic import validator, constr
from pydantic.main import BaseModel


class AdditionSchema(BaseModel):
    id: UUID
    full_name: constr(regex='^[a-zA-Zа-яА-Я\- | ]+$')
    balance: str
    hold: str
    status: bool


class DescriptionSchema(BaseModel):
    message: Union[str, List[dict]]


class ApiOutputSchema(BaseModel):
    """Схема вывода для api методов"""
    status: int
    result: Optional[bool]
    addition: Optional[AdditionSchema]
    description: Optional[DescriptionSchema]


class ApiAddInputSchema(BaseModel):
    """Схема ввода для api методов"""
    addition: int

    @validator('addition')
    def positive(cls, v):
        if v <= 0:
            raise ValueError('Insert a positive number')
        return v


class ApiSubstractInputSchema(BaseModel):
    """Схема ввода для api методов"""
    substraction: int

    @validator('substraction')
    def positive(cls, v):
        if v <= 0:
            raise ValueError('Insert a positive number')
        return v
