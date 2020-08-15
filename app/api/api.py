from fastapi import APIRouter
from app.api.endpoints import cumulatives

api_router = APIRouter()
api_router.include_router(cumulatives.router, prefix="/cumulatives")