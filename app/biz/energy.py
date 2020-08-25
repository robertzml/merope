"""
节能率计算
"""

import datetime
from app.db import water_heater


def equipment_energy_save(serial_number: str, date: str) -> float:
    """计算设备节能率

    :Parameters:
        - `serial_number`: 设备序列号.
        - `date`: 日志时间.
    """
    collection = water_heater.get_summary_cumulative()

    dt = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    # 前一天
    yestoday = dt + datetime.timedelta(days=-1)

    start = str(yestoday) + ' 00:00:00'
    end = str(yestoday) + ' 23:59:59'

    prev = collection.find_one({
        'device_serialnumber': serial_number,
        'log_time': {
            '$gte': start,
            '$lte': end
        }
    })

    # 今天
    today = collection.find_one({
        'device_serialnumber': serial_number,
        'log_time': {
            '$gte': start,
            '$lte': end
        }
    })

    if prev is None or today is None:
        return 0

    saving = today['cumulative_electricity_saving'] - yestoday[
        'cumulative_electricity_saving']
    using = today['cumulative_use_electricity'] - yestoday[
        'cumulative_use_electricity']

    energy_save = saving / (saving + using)
    return energy_save
