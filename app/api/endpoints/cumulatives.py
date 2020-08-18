from fastapi import APIRouter, Query
from app.models.cumulative import Cumulative
from app import biz

router = APIRouter()


@router.get("/day-first", response_model=Cumulative)
async def get_day_first(sn: str = Query(..., title="设备序列号"),
                        dt: str = Query(..., title="日期")) -> Cumulative:
    '''获取设备当日初始值
    '''

    dt = dt + ' 00:00:00'
    cum = biz.cumulative.get_day_first(sn, dt)

    return cum
