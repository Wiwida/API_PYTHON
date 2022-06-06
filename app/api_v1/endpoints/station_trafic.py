from fastapi import APIRouter, status
from app.db import supabase_methods

router = APIRouter()


@router.get("/api/all_traffic/{table}")
def read_traffic(table):
    all_station_traffic = supabase_methods.method_all_trafic(table)
    return all_station_traffic
