from pydantic import BaseModel, Field


class Cumulative(BaseModel):
    """
    热水器累积数据
    """

    # 设备序列号
    device_serialnumber: str = Field(..., title="设备序列号")

    mainboard_serialnumber: str

    log_time: str
    cumulative_heat_time: int
    cumulative_heat_water: int
    cumulative_duration_machine: int
    cumulative_use_electricity: int
    cumulative_electricity_saving: int
    cold_water_input_temp: int
    setting_temp: int
    comprehensive_electricity_saving: int
    energysave: int
