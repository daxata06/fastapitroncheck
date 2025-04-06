import pytest
from app.services.address_service import AddressService
from app.routers.router_models.response_models import AddressDataResponse


@pytest.mark.asyncio
async def test_save_and_retrieve_address(db_session):
    service = AddressService()

    test_address = AddressDataResponse(
        address="test_addr_1", energy=100.0, balance=50.0, bandwidth=10.0
    )

    await service.save(address_data=test_address, db=db_session)

    result = await service.get(db=db_session, skip=0, limit=1)

    assert len(result) == 1
    retrieved = result[0]
    assert retrieved.address == "test_addr_1"
    assert retrieved.energy == 100.0
    assert retrieved.balance == 50.0
    assert retrieved.bandwidth == 10.0
