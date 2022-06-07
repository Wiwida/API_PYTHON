from fastapi import APIRouter, Response
from app.db import supabase_methods
from app.schemas import schemas

router = APIRouter()


@router.get("/api/all_traffic/{table}")
def all_travellers(table: str, response: Response):
    try:
        all_station_travellers = supabase_methods.get_all(table)
        return all_station_travellers
    except:
        response.status_code = 404
        return "Problème de nom de table. Elle n'est peut-être pas réferencée ..."


@router.post("/api/all_trafic/{table}/add_element")
def add_traveller(table: str, traveller: schemas.addTraveller, response: Response):
    print(traveller)
    print(table)
    create_traveller = supabase_methods.create_traveller({table, traveller})
    try:

        return create_traveller
    except:
        response.status_code = 404
        return create_traveller

