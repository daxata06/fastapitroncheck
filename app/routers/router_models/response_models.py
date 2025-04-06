from pydantic import BaseModel


class AddressDataResponse(BaseModel):
    address: str
    balance: float
    energy: float
    bandwidth: float
