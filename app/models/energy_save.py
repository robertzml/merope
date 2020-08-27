from pydantic import Field, BaseModel
from datetime import date, datetime


class EnergySave(BaseModel):
    """设备节能率模型

    两天累积数差值
    """

    # 记录日期
    log_date: date = Field(datetime.now().date(), title="记录日期")

    prev_time: datetime = Field(datetime.now(), title="前一时刻")

    curr_time: datetime = Field(datetime.now(), title="当前时刻")

    cumulative_heat_time: int = Field(0, title="累积加热时间")

    cumulative_use_electricity: int = Field(0, title="累积用电量")

    cumulative_electricity_saving: int = Field(0, title="累计省电量")

    save_ratio: float = Field(0, title="节能率")
