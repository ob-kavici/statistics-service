import os

from fastapi import HTTPException
from supabase import Client, create_client
from core.config import *

def get_supabase_client(auth: dict = None) -> Client:
    supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    if auth:
        jwt = auth.get("jwt")
        refresh_token = auth.get("refresh_token")

        if not jwt:
            raise HTTPException(status_code=400, detail="Missing JWT in authentication.")
        if not refresh_token:
            raise HTTPException(status_code=400, detail="Missing Refresh Token in authentication.")

        try:
            supabase.auth.set_session(jwt, refresh_token)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to set session: {e}")
    
    return supabase

def get_rabbitmq_url():
    return f"amqp://{settings.RABBITMQ_USER}:{settings.RABBITMQ_PASS}@{settings.RABBITMQ_HOST}/"
