from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Il me reste a faire : Condition pour savoir quel table prendre et donc model
#                       Mettre la sécu en place
#                       Mettre tests en place
#                       RLS dans supabase mieux ?

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)


def get_all(payload):
    return supabase.table(payload).select('*').execute()


def create_traveller(payload):
    return supabase.table(payload[1]).insert(
        {
            'UIC': payload[0].UIC,
            'Gare': payload[0].Gare,
            'CSP': payload[0].CSP,
            'Pourcentage': payload[0].Pourcentage,
            'Annee': payload[0].Annee
        }
    ).execute()


def update_traveller(payload):
    return supabase.table(payload[1]).update({payload[2]: payload[3]}).eq('id', payload[0]).execute()


def delete_traveller(payload):
    return supabase.table(payload[1]).delete().eq('id', payload[0]).execute()
