from datetime import date
from decimal import Decimal
from typing import Optional
from enum import Enum

from pydantic import BaseModel


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class OperationsBase(BaseModel):
    date: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]


class Operations(OperationsBase):
    id: int

    class Config:
        orm_mode = True


class OperationCreate(OperationsBase):
    pass


class OperationUpdate(OperationsBase):
    pass
