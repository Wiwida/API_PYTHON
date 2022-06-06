from fastapi import APIRouter, status
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import json

load_dotenv()

router = APIRouter()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)


@router.get("/api/all_trafic")
async def read_trafic():
    all_station_trafic =  await supabase.table('gares_voyageurs_age').select('*').execute()
    decode = json.loads(str(all_station_trafic))
    return decode