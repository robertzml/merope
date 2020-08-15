from fastapi import APIRouter, Query
from app.models.cumulative import Cumulative

router = APIRouter()


@router.get("/", response_model=Cumulative)
async def read_cumulatives(sn: str = Query(..., title="设备序列号")) -> Cumulative:
    """
    获取设备当日初始值
    """
    doc = {
        "device_serialnumber": "0110358190706023",
        "mainboard_serialnumber": "10061907040294",
        "log_time": "2020-08-08 18:30:10",
        "cumulative_heat_time": 123,
        "cumulative_heat_water": 75847,
        "cumulative_duration_machine": 557410,
        "cumulative_use_electricity": 90211,
        "cumulative_electricity_saving": 66420,
        "cold_water_input_temp": 27,
        "setting_temp": 39,
        "comprehensive_electricity_saving": 66420,
        "energysave": 47
    }

    cum = Cumulative(**doc)
    return cum