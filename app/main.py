import aio_pika
from fastapi import FastAPI
from api.routes import router
from fastapi.middleware.cors import CORSMiddleware
from core.dependencies import get_supabase_client
from models.errors import *
from core.dependencies import *
from prometheus_client import Histogram, generate_latest, Counter
from contextlib import asynccontextmanager
from services.stats import consume_events
import asyncio

# Lifespan manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start the RabbitMQ consumer as a background task
    consume_task = asyncio.create_task(consume_events())
    print("Started consume task")
    try:
        yield
    finally:
        # Cancel the consume task on shutdown
        consume_task.cancel()
        try:
            await consume_task
        except asyncio.CancelledError:
            pass

app = FastAPI(lifespan=lifespan)

origins = [
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/stats", tags=["stats"])
app.router.lifespan_context = lifespan

# Metrics
request_count = Counter('http_requests_total', 'Total HTTP requests for stats-service')
response_time = Histogram('http_request_duration_seconds', 'Response time in seconds for stats-service')

@app.middleware("http")
async def metrics_middleware(request, call_next):
    request_count.inc()
    with response_time.time():
        response = await call_next(request)
    return response

@app.get("/metrics")
def metrics():
    return generate_latest()

@app.get("/", responses={200: {"model": dict}})
async def read_root():
    return {"service": "stats-service"}

@app.get("/health/liveness", responses={200: {"model": dict}})
async def liveness():
    return {"status": "alive"}

@app.get("/health/readiness", responses={
    200: {"model": dict},
    500: {"model": InternalServerError}
})
async def readiness():
    return {"status": "ready"}
