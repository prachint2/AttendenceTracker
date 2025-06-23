from pydantic import BaseModel
from typing import Optional

class Record(BaseModel):
    id: int
    name: str
    age: int
    is_present: bool


class AbsentTracker(BaseModel):
    is_present: Optional[bool] = None



class Roster(BaseModel):
    name: str

    class Config:
        from_attributes = True

