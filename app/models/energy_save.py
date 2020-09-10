from pydantic import Field, BaseModel
from typing import Optional
from datetime import date, datetime


class EnergySave(BaseModel):
    """设备节能率模型

    两天累积数差值
    """

    # 设备序列号
    serial_number: str = Field('', title="设备序列号")

    # 记录日期
    log_date: date = Field(datetime.now().date(), title="记录日期")

    prev_time: Optional[datetime] = Field(None, title="前一时刻")

    curr_time: Optional[datetime] = Field(None, title="当前时刻")

    cumulative_heat_time: int = Field(0, title="累积加热时间")

    cumulative_use_electricity: int = Field(0, title="累积用电量")

    cumulative_electricity_saving: int = Field(0, title="累计省电量")

    cumulative_heat_water: int = Field(0, title="累计使用热水量")

    cumulative_duration_machine: int = Field(0, title="累计使用时间")

    save_ratio: float = Field(0, title="节能率")

    execpt_value: int = Field(0, title='数据异常状态，0表示正常')

    utctime: Optional[datetime]

    def keys(self):
        return ('serial_number', 'log_date', 'prev_time', 'curr_time',
                'cumulative_heat_time', 'cumulative_use_electricity',
                'cumulative_electricity_saving', 'cumulative_heat_water',
                'cumulative_duration_machine', 'save_ratio', 'utctime')

    def __getitem__(self, item):
        if item == 'log_date':
            return str(self.log_date)
        return getattr(self, item)
