from fastapi import APIRouter, Query
from app.models.cumulative import Cumulative
from app import biz

router = APIRouter()


@router.get("/", response_model=Cumulative)
async def read_cumulatives(sn: str = Query(..., title="设备序列号")) -> Cumulative:
    '''
    获取设备当日初始值
    '''
    cum = biz.cumulative.get_day_first(sn)
    return cum
