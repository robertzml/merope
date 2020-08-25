from fastapi import APIRouter
from app.api.endpoints import cumulatives, dispatchs, energys

api_router = APIRouter()
api_router.include_router(cumulatives.router, prefix="/cumulatives")
api_router.include_router(dispatchs.router, prefix="/dispatchs")
api_router.include_router(energys.router, prefix="/energys")