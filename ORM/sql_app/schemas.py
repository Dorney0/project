from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        from_attributes = True


class FlowerBase(BaseModel):
    name: str
    image_url: str
    price: int


class FlowerCreate(FlowerBase):
    pass


class FlowerUpdate(BaseModel):
    name: Optional[str] = None
    image_url: Optional[str] = None
    price: Optional[int] = None


class Flower(FlowerBase):
    id: int

    class Config:
        from_attributes = True
