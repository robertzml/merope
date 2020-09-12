"""
周节能率计算
"""

import datetime
import pytz
from app.db import water_heater
from app.models.week_save import WeekSave


def equipment_week_save(serial_number: str, date: str) -> WeekSave:
    """计算设备周节能率

    处理指定日期的上一周

    :Parameters:
        - `serial_number`: 设备序列号.
        - `date`: 日期.
    """

    collection = water_heater.get_summary_cumulative()

    tz = pytz.timezone('Asia/Shanghai')

    week_save = WeekSave()
    week_save.serial_number = serial_number

    current_day = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    # 上上周最后一天
    last_week_start = current_day - datetime.timedelta(
        days=current_day.weekday() + 8)

    start = str(last_week_start) + ' 00:00:00'
    end = str(last_week_start) + ' 23:59:59'

    prev = collection.find_one({
        'device_serialnumber': serial_number,
        'log_time': {
            '$gte': start,
            '$lte': end
        }
    })

    # 上周最后一天
    last_week_end = current_day - datetime.timedelta(
        days=current_day.weekday() + 1)

    start = str(last_week_end) + ' 00:00:00'
    end = str(last_week_end) + ' 23:59:59'

    curr = collection.find_one({
        'device_serialnumber': serial_number,
        'log_time': {
            '$gte': start,
            '$lte': end
        }
    })

    if prev is None or curr is None:
        return None

    # 赋值
    week_save.log_date = str(last_week_end)
    week_save.prev_time = datetime.datetime.strptime(prev['log_time'],
                                                     "%Y-%m-%d %H:%M:%S")
    week_save.curr_time = datetime.datetime.strptime(curr['log_time'],
                                                     "%Y-%m-%d %H:%M:%S")

    week_save.prev_time = week_save.prev_time.replace(tzinfo=tz)
    week_save.curr_time = week_save.curr_time.replace(tzinfo=tz)

    week_save.cumulative_electricity_saving = curr[
        'cumulative_electricity_saving'] - prev['cumulative_electricity_saving']
    week_save.cumulative_use_electricity = curr[
        'cumulative_use_electricity'] - prev['cumulative_use_electricity']
    week_save.cumulative_heat_time = curr['cumulative_heat_time'] - prev[
        'cumulative_heat_time']
    week_save.cumulative_heat_water = curr['cumulative_heat_water'] - prev[
        'cumulative_heat_water']
    week_save.cumulative_duration_machine = curr[
        'cumulative_duration_machine'] - prev['cumulative_duration_machine']

    if week_save.cumulative_electricity_saving + week_save.cumulative_use_electricity == 0:
        week_save.save_ratio = 0
    else:
        week_save.save_ratio = round(
            week_save.cumulative_electricity_saving /
            (week_save.cumulative_electricity_saving +
             week_save.cumulative_use_electricity) * 100, 2)

    if week_save.cumulative_heat_time < 0 or week_save.cumulative_heat_water < 0 or \
            week_save.cumulative_duration_machine < 0 or week_save.cumulative_use_electricity < 0 or \
            week_save.cumulative_electricity_saving < 0:
        week_save.is_valid = 1

    week_save.utctime = datetime.datetime.utcnow()

    return week_save


def save_to_summary(data: WeekSave) -> None:
    """保存节能数据到数据库

    Args:
        data: 节能数据
    """
    collection = water_heater.get_summary_week_save()

    exist: int = collection.find({
        'serial_number': data.serial_number,
        'log_date': str(data.log_date)
    }).count()

    if exist > 0:
        return
    else:
        collection.insert_one(dict(data))

    return
