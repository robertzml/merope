from fastapi import APIRouter, Query, BackgroundTasks
from typing import Optional
from app import biz
from app.models.energy_save import EnergySave

router = APIRouter()


@router.get('/day-save', response_model=EnergySave)
async def get_equipment_energy_save(sn: str = Query(..., title="设备序列号"),
                                    dt: str = Query(..., title="日期"),
                                    save: Optional[int] = Query(
                                        None,
                                        title="是否保存",
                                        description="1为保存到汇总表")) -> EnergySave:
    """计算设备指定日节能率
    """

    energy_save = biz.energy.equipment_energy_save(sn, dt)
    if energy_save is None:
        return None

    # print(dict(energy_save))

    if save == 1:
        biz.energy.save_to_summary(energy_save)

    return energy_save


@router.get('/daily-process')
async def daily_process(background_tasks: BackgroundTasks,
                        dt: str = Query(..., title="日期")):
    """处理每日节能率数据
    """

    background_tasks.add_task(biz.energy.daily_process, dt)
    return {"message", "ok"}
