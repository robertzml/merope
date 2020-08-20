from fastapi import APIRouter
from app.api.endpoints import cumulatives, dispatchs

api_router = APIRouter()
api_router.include_router(cumulatives.router, prefix="/cumulatives")
api_router.include_router(dispatchs.router, prefix="/dispatchs")
