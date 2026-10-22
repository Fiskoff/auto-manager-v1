from datetime import date

from pydantic import BaseModel, Field, ConfigDict


class CarBase(BaseModel):
    car_brand: str = Field(max_length=32)
    model: str = Field(max_length=64)
    year: int = Field(ge=1960, le=2060)
    color: str = Field(max_length=64)
    reg_number: str = Field(max_length=9)
    mileage: int | None = Field(default=None)
    last_service_date: date | None = Field(default=None)


class CarCreate(CarBase):
    pass


class CarResponse(CarBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class CarUpdate(BaseModel):
    color: str | None = Field(max_length=64, default=None)
    reg_number: str | None = Field(max_length=9, default=None)
    mileage: int | None = Field(default=None)
    last_service_date: date | None = Field(default=None)

