from fastapi import APIRouter, Query, BackgroundTasks
from typing import Optional
from app.models.cumulative import Cumulative
from app import biz

router = APIRouter()


@router.get("/day-first", response_model=Cumulative)
async def get_day_first(sn: str = Query(..., title="设备序列号"),
                        dt: str = Query(..., title="日期")) -> Cumulative:
    """获取设备当日初始值
    """

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

    cum = biz.cumulative.get_day_last(sn, dt)

    if save == 1:
        biz.cumulative.save_to_summary(cum)

    return cum


@router.get("/avg-cold", response_model=float)
async def get_avg_cold_temp(sn: str = Query(..., title="设备序列号"),
                            dt: str = Query(..., title="日期")) -> float:
    """获取设备冷水平均进水温度
    """

    avg = biz.cumulative.calculateAvgColdTemp(sn, dt)
    return avg


@router.get("/daily-process")
async def daily_process(background_tasks: BackgroundTasks,
                        dt: str = Query(..., title="日期")):
    """处理每日累积数据
    """

    background_tasks.add_task(biz.cumulative.daily_process, dt)
    return {'message': 'ok'}
