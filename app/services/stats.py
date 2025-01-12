import json
import aio_pika
import asyncio
from core.dependencies import *

async def consume_events():
    connection = await aio_pika.connect_robust(get_rabbitmq_url())
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("game.states", durable=True)
        async for message in queue:
            async with message.process():
                event_data = json.loads(message.body)
                await process_event(event_data)

async def process_event(event_data: dict):
    print("Processing event:", event_data)
    # supabase = await get_supabase_client()
    # Store raw event
    # await supabase.execute("INSERT INTO events (data) VALUES ($1)", json.dumps(event_data))
    # Update stats
    # await update_stats(event_data)

async def update_stats(event_data: dict):
    # Update stats logic, e.g., increment counters in the database
    supabase = await get_supabase_client()
    game_id = event_data["game_id"]
    user_id = event_data["user_id"]
    await supabase.execute("INSERT INTO game_statistics (game_id, user_id) VALUES ($1, $2)", game_id, user_id)

async def get_stats():
    supabase = await get_supabase_client()
    response = await supabase.execute("SELECT * FROM game_statistics")
    return response["data"]