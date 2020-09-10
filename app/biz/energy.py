"""
节能率计算
"""

import datetime
import pytz
from app.db import water_heater
from app.models.energy_save import EnergySave
from . import equipment


def equipment_energy_save(serial_number: str, date: str) -> EnergySave:
    """计算设备节能率

    :Parameters:
        - `serial_number`: 设备序列号.
        - `date`: 日期.
    """
    collection = water_heater.get_summary_cumulative()

    energy_save = EnergySave()

    tz = pytz.timezone('Asia/Shanghai')

    energy_save.serial_number = serial_number
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
        return None

    energy_save.prev_time = datetime.datetime.strptime(prev['log_time'],
                                                       "%Y-%m-%d %H:%M:%S")
    energy_save.curr_time = datetime.datetime.strptime(today['log_time'],
                                                       "%Y-%m-%d %H:%M:%S")

    energy_save.prev_time = energy_save.prev_time.replace(tzinfo=tz)
    energy_save.curr_time = energy_save.curr_time.replace(tzinfo=tz)

    energy_save.cumulative_electricity_saving = today[
        'cumulative_electricity_saving'] - prev['cumulative_electricity_saving']
    energy_save.cumulative_use_electricity = today[
        'cumulative_use_electricity'] - prev['cumulative_use_electricity']
    energy_save.cumulative_heat_time = today['cumulative_heat_time'] - prev[
        'cumulative_heat_time']
    energy_save.cumulative_heat_water = today['cumulative_heat_water'] - prev[
        'cumulative_heat_water']
    energy_save.cumulative_duration_machine = today[
        'cumulative_duration_machine'] - prev['cumulative_duration_machine']

    if energy_save.cumulative_electricity_saving + energy_save.cumulative_use_electricity == 0:
        energy_save.save_ratio = 0
    else:
        energy_save.save_ratio = round(
            energy_save.cumulative_electricity_saving /
            (energy_save.cumulative_electricity_saving +
             energy_save.cumulative_use_electricity) * 100, 2)

    if energy_save.cumulative_heat_time < 0 or energy_save.cumulative_heat_water < 0 or \
            energy_save.cumulative_duration_machine < 0 or energy_save.cumulative_use_electricity < 0 or \
            energy_save.cumulative_electricity_saving < 0:
        energy_save.execpt_value = -1

    energy_save.utctime = datetime.datetime.utcnow()

    return energy_save


def save_to_summary(data: EnergySave) -> None:
    """保存节能数据到数据库

    Args:
        data: 节能数据
    """
    collection = water_heater.get_summary_save()

    exist: int = collection.find({
        'serial_number': data.serial_number,
        'log_date': str(data.log_date)
    }).count()

    if exist > 0:
        return
    else:
        collection.insert_one(dict(data))

    return


def daily_process(log_time: str) -> None:
    """处理指定日所有设备节能率数据

    计算节能率相关数据，保存到数据库
    Args:
        log_imte: 日期
    """

    equipment_list = equipment.get_all()

    for item in equipment_list:
        es = equipment_energy_save(item.device_serialnumber, log_time)
        if es is not None:
            save_to_summary(es)
            # print('date: %s, equipment: %s energy save ratio save' %
            #      (log_time, es.serial_number))

    print('energy save biz daily process finish')
    return
