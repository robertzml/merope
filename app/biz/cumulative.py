'''
累积数据操作业务
'''

from app.models.cumulative import Cumulative
from app.db import water_heater


def get_day_first(serial_number: str, log_time: str) -> Cumulative:
    """获取设备当日第一条累积记录

    :Parameters:
        - `serial_number`: 设备序列号.
        - `log_time`: 日志时间.
    """

    collection = water_heater.get_cumulative_collection()

    filter = {
        'device_serialnumber': serial_number,
        'log_time': {
            '$gte': log_time
        }
    }
    sort = [('log_time', 1)]
    data = collection.find_one(filter, sort=sort)

    if data is None:
        return None
    else:
        cum = Cumulative(**data)
        return cum


def get_day_last(serial_number: str, log_time: str) -> Cumulative:
    """获取设备当日最后一条累积记录

    :Parameters:
        - `serial_number`: 设备序列号.
        - `log_time`: 日志时间.
    """

    collection = water_heater.get_cumulative_collection()

    filter = {
        'device_serialnumber': serial_number,
        'log_time': {
            '$lte': log_time
        }
    }
    sort = [('log_time', -1)]
    data = collection.find_one(filter, sort=sort)

    if data is None:
        return None
    else:
        cum = Cumulative(**data)
        return cum
