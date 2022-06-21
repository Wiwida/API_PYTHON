from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_all_travellers():
    response = client.get("/api/all_trafic/GARES_VOYAGEURS_CSP")
