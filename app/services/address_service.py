from app.routers.router_models.response_models import AddressDataResponse
from app.models.address_data import AddressData
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List


class AddressService:
    async def save(
        self,
        address_data: AddressDataResponse,
        db: AsyncSession,
    ) -> None:
        data = AddressData(
            address=address_data.address,
            energy=address_data.energy,
            balance=address_data.balance,
            bandwidth=address_data.bandwidth,
        )
        db.add(data)
        await db.commit()
        await db.refresh(data)

    async def get(
        self,
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
    ) -> List[AddressData]:
        command = select(AddressData).offset(skip).limit(limit)
        result = await db.execute(command)
        return result.scalars().all()
