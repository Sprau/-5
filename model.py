from pydantic import BaseModel

class Pet(BaseModel):
    id: int
    category_id: int
    name: str
    photo_urls: list
    tags: list
    status: str