from pydantic import BaseModel


class addTraveller(BaseModel):
    UIC: int
    Gare: str
    CSP: str
    Pourcentage: float
    Annee: int
