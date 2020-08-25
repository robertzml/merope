from fastapi import APIRouter, Query
from app import biz

router = APIRouter()


@router.get('/day-save')
async def get_equipment_energy_save(sn: str = Query(..., title="设备序列号"),
                                    dt: str = Query(..., title="日期")):
    """计算设备指定日节能率
    """

    energy_save = biz.energy.equipment_energy_save(sn, dt)

    return {'energy_save': energy_save, "serial_number": sn, "date": dt}
