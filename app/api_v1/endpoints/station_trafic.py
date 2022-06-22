from fastapi import APIRouter, Response
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from datetime import timedelta

from app.db.supabase_methods import MethodSupabase
from app.schemas import schemas
from app.db.security_const import ACCESS_TOKEN_EXPIRE_MINUTES
from app.db.security import get_current_active_user, authenticate_user, create_access_token, get_password_hash


router = APIRouter()


# Routes

# AUTH
@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    userfromdb = MethodSupabase(nametable='USERS', username=form_data.username).get_userdb()
    user = authenticate_user(userfromdb.data[0], form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    # ADD NEW HASH PASSWORD FOR USER (SAFE)
    method_user = MethodSupabase(username=user.username, nametable='USERS', targetcolumnnewvalue=get_password_hash(form_data.password), targetcolumn='hashed_password')
    method_user.update_hashedpassword_user()

    return {"access_token": access_token, "token_type": "bearer"}


# GET ALL TRAVELLER
@router.get("/api/all_traffic/{table}")
async def all_travellers(table: str, response: Response, current_user: schemas.User = Depends(get_current_active_user)):
    try:
        all_station_travellers = MethodSupabase(nametable=table).get_all()
        response.status_code = 200
        return all_station_travellers
    except:
        response.status_code = 404
        return "Un problème est survenu ..."


# GET TRAVELLER
@router.get("/api/all_traffic/{table}/{idtraveller}")
async def get_one(table: str, idtraveller: int, response: Response,
                  current_user: schemas.User = Depends(get_current_active_user)):
    try:
        all_station_travellers = MethodSupabase(nametable=table, idtraveller=idtraveller).get_one()
        response.status_code = 200
        return all_station_travellers
    except:
        response.status_code = 404
        return "Un problème est survenu ..."


# ADD TRAVELLER
@router.post("/api/all_trafic/{table}/add_element")
async def add_traveller(table: str, traveller: schemas.Travellers, response: Response,
                        current_user: schemas.User = Depends(get_current_active_user)):
    try:
        create_traveller = MethodSupabase(nametable=table, trafictraveller=traveller).create_traveller()
        response.status_code = 200
        return create_traveller
    except:
        response.status_code = 404
        return "Un problème est survenu ..."


# DELETE TRAVELLER
@router.delete("/api/all_trafic/{table}/delete_element/{idtraveller}")
async def delete_traveller(table: str, idtraveller: int, response: Response,
                           current_user: schemas.User = Depends(get_current_active_user)):
    try:
        MethodSupabase(idtraveller=idtraveller, nametable=table).delete_traveller()
        response.status_code = 200
        return 'Utilisateur supprimé !'
    except:
        response.status_code = 404
        return "Un problème est survenu ..."


# UPDATE TRAVELLER
@router.patch("/api/all_trafic/{table}/update_element/{idtraveller}")
async def update_traveller(table: str, idtraveller: int, column: str, newvalue: str, response: Response,
                           current_user: schemas.User = Depends(get_current_active_user)):
    try:
        updated_traveller = \
            MethodSupabase(
                idtraveller=idtraveller,
                nametable=table,
                targetcolumnnewvalue=newvalue,
                targetcolumn=column) \
                .update_traveller()
        response.status_code = 200
        return updated_traveller
    except:
        response.status_code = 404
        return "Un problème est survenu ..."
