from fastapi import APIRouter, Depends, HTTPException, Header, Query
from typing import Optional
import services.stats as StatsService
from models.gamestate import *
from models.errors import *
from models.stats import *
from core.dependencies import get_supabase_client

router = APIRouter()

async def get_auth_headers(
    authorization: Optional[str] = Header(None),
    x_refresh_token: Optional[str] = Header(None),
) -> dict:
    if not authorization or not x_refresh_token:
        raise HTTPException(
            status_code=400,
            detail="Missing JWT or Refresh Token in headers"
        )

    jwt = authorization.replace("Bearer ", "")
    return {"jwt": jwt, "refresh_token": x_refresh_token}

@router.get("/stats", responses={
    200: {"model": list[GameStats], "description": "List of all game statistics"},
    400: {"model": ValidationError, "description": "Invalid query parameters provided"},
    404: {"model": NotFoundError, "description": "No game statistics found"}
})
async def get_stats():
    return StatsService.get_stats()
