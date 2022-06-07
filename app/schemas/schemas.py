from pydantic import BaseModel


class addTraveller(BaseModel):
    UIC: int
    station: str
    CSP: str
    percentage: float
    year: int
