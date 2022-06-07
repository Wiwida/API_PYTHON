from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)


def get_all(payload):
    return supabase.table(payload).select('*').execute()


def create_traveller(payload):
    print('heyyyyy : ', payload)
    return supabase.table(payload.table).insert(
        {
            'UIC': payload.traveller.UIC,
            'Gare': payload.traveller.station,
            'CSP': payload.traveller.CSP,
            'Pourcentage': payload.traveller.percentage,
            'Année': payload.traveller.year
        }
    ).execute()
