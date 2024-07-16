import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from datetime import datetime

@pytest.mark.asyncio
async def test_greatings():
    transport = ASGITransport(app=app)
    fecha = datetime.now()
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert f"<h1>Bienvenido! hoy es {fecha.day} del mes {fecha.month} del {fecha.year}</h1>" in response.text
    assert "https://www.linkedin.com/in/oarf/" in response.text