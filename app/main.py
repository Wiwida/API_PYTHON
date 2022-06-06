from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api_v1.endpoints import station_trafic

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


@app.get("/")
async def root():
    return {"status": "OK"}
