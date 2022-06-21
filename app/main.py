import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.api_v1.endpoints import station_trafic

app = FastAPI()
app.include_router(station_trafic.router)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Middleware

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# Init


@app.get("/")
async def root():
    return {"OK": "tout est ok"}
