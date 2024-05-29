from pydantic import BaseModel
from typing import Optional

class STastAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STastAdd):
    id: int