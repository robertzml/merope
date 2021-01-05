from pydantic import Field, BaseModel
from typing import Optional
from datetime import datetime


class WeekSave(BaseModel):
    """设备每周节能率模型

    上周最后一条和本周最后一条累积数差值
    """

    # 设备序列号
    serial_number: str = Field('', title="设备序列号")

    # 周节能率的最后一天
    log_date: str = Field('', title="结束日期")

    prev_time: Optional[datetime] = Field(None, title="前一时刻")

    curr_time: Optional[datetime] = Field(None, title="当前时刻")

    cumulative_heat_time: int = Field(0, title="累积加热时间")

    cumulative_use_electricity: int = Field(0, title="累积用电量")

    cumulative_electricity_saving: int = Field(0, title="累计省电量")

    cumulative_heat_water: int = Field(0, title="累计使用热水量")

    cumulative_duration_machine: int = Field(0, title="累计使用时间")

    save_ratio: float = Field(0, title="节能率")

    is_valid: int = Field(0, title='数据异常状态，0表示正常')

    utctime: Optional[datetime]
