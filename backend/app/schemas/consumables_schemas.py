from datetime import date

from pydantic import BaseModel, Field, ConfigDict


class ConsumablesBase(BaseModel):
    name: str = Field(max_length=128)
    description: str | None = Field(max_length= 256, default=None)
    start_mileage: int
    end_mileage: int | None = Field(default=None)
    start_date: date
    end_date: date | None = Field(default=None)
    car_id: int


class ConsumablesCreate(ConsumablesBase):
    pass


class ConsumablesResponse(ConsumablesBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ConsumablesResponseList(ConsumablesBase):
    consumables: list[ConsumablesResponse]


class ConsumablesUpdate(BaseModel):
    description: str | None = Field(max_length= 256, default=None)
    start_mileage: int | None = Field(default=None)
    end_mileage: int | None = Field(default=None)
    start_date: date | None = Field(default=None)
    end_date: date | None = Field(default=None)