
from fastapi import APIRouter, status
from supabase import create_client, Client
# from dotenv import load_dotenv
import os

# load_dotenv()

router = APIRouter()

url = os.environ.get("URL")
key = os.environ.get("KEY")

supabase: Client = create_client(url, key)


@app.get("/")
def index():
  return {"message": "Hello World"}

@router.get("/api/all_trafic")
async def read_trafic():
    all_station_trafic =  await supabase.table('GARES_VOYAGEURS_CSP').select('*').execute()
    return all_station_trafic