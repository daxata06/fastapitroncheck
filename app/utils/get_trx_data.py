from tronpy import AsyncTron
from tronpy.keys import PrivateKey
from app import settings
from app.expections.address_not_fount_expection import AddressNotFoundError

priv_key = PrivateKey(bytes.fromhex(settings.PRIVATE_KEY))


async def get_data(address: str) -> dict:
    async with AsyncTron(network="nile") as client:
        try:
            bandwidth = await client.get_bandwidth(addr=address)
            balance = await client.get_account_balance(addr=address)
            energy = await get_energy(address=address)
        except:  # noqa
            raise AddressNotFoundError

        return {
            "bandwidth": bandwidth,
            "balance": balance,
            "energy": energy,
        }


async def get_energy(address: str) -> float:
    async with AsyncTron(network="nile") as client:
        resources = await client.get_account_resource(address)
        energy_limit = resources.get("EnergyLimit", 0)
        energy_used = resources.get("EnergyUsed", 0)
        available_energy = energy_limit - energy_used

        return available_energy
