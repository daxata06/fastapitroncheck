from fastapi import APIRouter, HTTPException, Depends
from app.routers.router_models.request_models import Address
from app.routers.router_models.response_models import AddressDataResponse
from starlette import status
from app.utils.get_trx_data import get_data
from app.models.session import get_db
from app.services.address_service import AddressService
from app.expections.address_not_fount_expection import AddressNotFoundError
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.address_data import AddressData
from typing import List


router = APIRouter(prefix="/addressdata")


@router.post(
    "/address", response_model=AddressDataResponse, status_code=status.HTTP_200_OK
)
async def address(
    address: Address,
    db: AsyncSession = Depends(get_db),
) -> AddressDataResponse:
    try:
        address_data = await get_data(address=address.address)
        data = AddressDataResponse(
            address=address.address,
            energy=address_data["energy"],
            balance=address_data["balance"],
            bandwidth=address_data["bandwidth"],
        )
        address_service = AddressService()
        await address_service.save(address_data=data, db=db)
        return data

    except AddressNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Address not found"
        )


@router.get("/history", response_model=List[AddressDataResponse])
async def history(
    db: AsyncSession = Depends(get_db),
    limit: int = 100,
    offset: int = 0,
) -> List[AddressData]:
    address_service = AddressService()
    history = await address_service.get(db=db, skip=offset, limit=limit)
    return history
