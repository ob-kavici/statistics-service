from datetime import datetime
from pydantic import BaseModel

class GameStats(BaseModel):
    id: int
    player_name: str
    score: int
    level: int
    time_played: float
    date: datetime

    class Config:
        orm_mode = True