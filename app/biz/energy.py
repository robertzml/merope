"""
节能率计算
"""

import datetime
from app.db import water_heater
from app.models.energy_save import EnergySave


def equipment_energy_save(serial_number: str, date: str) -> EnergySave:
    """计算设备节能率

    :Parameters:
        - `serial_number`: 设备序列号.
        - `date`: 日期.
    """
    collection = water_heater.get_summary_cumulative()

    energy_save = EnergySave()

    energy_save.log_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    # 前一天
    yestoday = energy_save.log_date + datetime.timedelta(days=-1)

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
    start = date + ' 00:00:00'
    end = date + ' 23:59:59'

    today = collection.find_one({
        'device_serialnumber': serial_number,
        'log_time': {
            '$gte': start,
            '$lte': end
        }
    })

    if prev is None or today is None:
        return 0

    energy_save.prev_time = datetime.datetime.strptime(prev['log_time'],
                                                       "%Y-%m-%d %H:%M:%S")
    energy_save.curr_time = datetime.datetime.strptime(today['log_time'],
                                                       "%Y-%m-%d %H:%M:%S")

    energy_save.cumulative_electricity_saving = today[
        'cumulative_electricity_saving'] - prev['cumulative_electricity_saving']
    energy_save.cumulative_use_electricity = today[
        'cumulative_use_electricity'] - prev['cumulative_use_electricity']
    energy_save.cumulative_heat_time = today['cumulative_heat_time'] - prev[
        'cumulative_heat_time']

    energy_save.save_ratio = round(
        energy_save.cumulative_electricity_saving /
        (energy_save.cumulative_electricity_saving +
         energy_save.cumulative_use_electricity) * 100, 2)
    return energy_save
