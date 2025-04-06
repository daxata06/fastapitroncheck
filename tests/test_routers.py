import pytest
from fastapi import status


@pytest.mark.anyio
async def test_create_address_success(client):
    test_data = {
        "address": "TYLQpFEmxEGQpWh2He3csjNsKdC2jRyWRF",
    }

    response = client.post("/addressdata/address", json=test_data)
    print(response)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["energy"] is not None
