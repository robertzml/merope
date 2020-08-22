from fastapi import APIRouter, Query
from typing import Optional
from app.models.cumulative import Cumulative
from app import biz

router = APIRouter()


@router.get("/day-first", response_model=Cumulative)
async def get_day_first(sn: str = Query(..., title="设备序列号"),
                        dt: str = Query(..., title="日期")) -> Cumulative:
    """获取设备当日初始值
    """

    dt = dt + ' 00:00:00'
    cum = biz.cumulative.get_day_first(sn, dt)

    return cum


@router.get("/day-last", response_model=Cumulative)
async def get_day_last(sn: str = Query(..., title="设备序列号"),
                       dt: str = Query(..., title="日期"),
                       save: Optional[int] = Query(
                           None, title="是否保存",
                           description="1为保存到汇总表")) -> Cumulative:
    """获取设备当日最终值
    """

    dt = dt + ' 23:59:59'
    cum = biz.cumulative.get_day_last(sn, dt)

    if save == 1:
        biz.cumulative.save_to_summary(cum)

    return cum
