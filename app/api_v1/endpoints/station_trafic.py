from fastapi import APIRouter, Response
from app.db import supabase_methods
from app.schemas import schemas

router = APIRouter()


@router.get("/api/all_traffic/{table}")
async def all_travellers(table: str, response: Response):
    try:
        all_station_travellers = await supabase_methods.get_all(table)
        return all_station_travellers
    except:
        response.status_code = 404
        return "Problème de nom de table. Elle n'est peut-être pas réferencée ..."


@router.post("/api/all_trafic/{table}/add_element")
async def add_traveller(table: str, traveller: schemas.addTraveller, response: Response):

    try:
        create_traveller = await supabase_methods.create_traveller([traveller, table])
        return create_traveller
    except:
        response.status_code = 404
        return 'toto'


@router.delete("/api/all_trafic/{table}/delete_element")
async def delete_traveller(table: str, id: int, response : Response):

    try:
        await supabase_methods.delete_traveller([id, table])
        return 'Utilisateur supprimé !'
    except:
        response.status_code = 404
        return 'toto2'


@router.patch("/api/all_trafic/{table}/update_element")
async def update_traveller(table: str, id: int, column: str, newvalue, response : Response):

    try:
        updated_traveller = await supabase_methods.update_traveller([id, table, column, newvalue])
        return updated_traveller
    except:
        response.status_code = 404
        return 'toto2'
