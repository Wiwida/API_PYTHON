from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)


class MethodSupabase:

    def __init__(self, nametable, idtraveller=None, trafictraveller=None, targetcolumn=None, targetcolumnnewvalue=None, username=None):
        self.nametable = nametable
        self.idtraveller = idtraveller
        self.traficTraveller = trafictraveller
        self.targetcolumn = targetcolumn
        self.targetcolumnnewvalue = targetcolumnnewvalue
        self.username = username

    def update_hashedpassword_user(self):
        return supabase.table(self.nametable).update({self.targetcolumn: self.targetcolumnnewvalue}).eq('username', self.username).execute()

    def get_userdb(self):
        return supabase.table(self.nametable).select('*').eq('username', self.username).execute()

    def get_one(self):
        return supabase.table(self.nametable).select('*').eq('id', self.idtraveller).execute()

    def get_all(self):
        return supabase.table(self.nametable).select('*').execute()

    def create_traveller(self):
        return supabase.table(self.nametable).insert(
            {
                'UIC': self.traficTraveller.UIC,
                'Gare': self.traficTraveller.Gare,
                'CSP': self.traficTraveller.CSP,
                'Pourcentage': self.traficTraveller.Pourcentage,
                'Annee': self.traficTraveller.Annee
            }
        ).execute()

    def update_traveller(self):
        return supabase.table(self.nametable).update({self.targetcolumn: self.targetcolumnnewvalue}).eq('id', self.idtraveller).execute()

    def delete_traveller(self):
        return supabase.table(self.nametable).delete().eq('id', self.idtraveller).execute()

