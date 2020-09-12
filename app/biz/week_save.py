"""
周节能率计算
"""

import datetime
# from app.db import water_heater
from app.models.week_save import WeekSave


def equipment_week_save(serial_number: str, week: int) -> WeekSave:
    """计算设备周节能率

    :Parameters:
        - `serial_number`: 设备序列号.
        - `week`: 第几周.
    """

    # collection = water_heater.get_summary_week_save()

    week_save = WeekSave()
    week_save.serial_number = serial_number
    week_save.week = week

    year = datetime.datetime.now().year

    year_first = datetime.date(year, 1, 1).isocalendar()

    return week_save
