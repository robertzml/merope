from pydantic import Field, BaseModel


class Cumulative(BaseModel):
    '''
    热水器累积数据
    '''

    device_serialnumber: str = Field(..., title="设备序列号")

    mainboard_serialnumber: str = Field(..., title="主板序列号")

    log_time: str = Field(..., title="记录时间")

    cumulative_heat_time: int = Field(..., title="累积加热时间")

    cumulative_heat_water: int = Field(..., title="累计使用热水量")
    cumulative_duration_machine: int
    cumulative_use_electricity: int
    cumulative_electricity_saving: int
    cold_water_input_temp: int
    setting_temp: int
    comprehensive_electricity_saving: int
    energysave: int = Field(..., title="节能率")
