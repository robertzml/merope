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

    cumulative_duration_machine: int = Field(..., title="累计使用时间")

    cumulative_use_electricity: int = Field(..., title="累计用电量")

    cumulative_electricity_saving: int = Field(..., title="累计省电量")

    cold_water_input_temp: int = Field(..., title="冷水进水温度")

    avgcoldtemp: int = Field(..., title="平均冷水进水温度")

    setting_temp: int
    comprehensive_electricity_saving: int
    energysave: int = Field(..., title="节能率")
