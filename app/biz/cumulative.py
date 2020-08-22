'''
累积数据操作业务
'''

from app.models.cumulative import Cumulative
from app.db import water_heater
from . import equipment


def get_day_first(serial_number: str, log_time: str) -> Cumulative:
    """获取设备当日第一条累积记录

    :Parameters:
        - `serial_number`: 设备序列号.
        - `log_time`: 日志时间.
    """

    collection = water_heater.get_cumulative_collection()

    end = log_time + ' 23:59:59'
    start = log_time + ' 00:00:00'

    filter = {
        'device_serialnumber': serial_number,
        'log_time': {
            '$gte': start,
            '$lte': end
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

    end = log_time + ' 23:59:59'
    start = log_time + ' 00:00:00'

    filter = {
        'device_serialnumber': serial_number,
        'log_time': {
            '$gte': start,
            '$lte': end
        }
    }
    sort = [('log_time', -1)]
    data = collection.find_one(filter, sort=sort)

    if data is None:
        return None
    else:
        cum = Cumulative(**data)
        return cum


def save_to_summary(cum: Cumulative):
    """保存设备累积记录到每日汇总表
    """

    collection = water_heater.get_summary_cumulative()

    exist: int = collection.find({
        'device_serialnumber': cum.device_serialnumber,
        'log_time': cum.log_time
    }).count()

    if exist > 0:
        # print('equipment %s summary exist.' % cum.device_serialnumber)
        return

    collection.insert_one(cum.__dict__)
    return


def daily_process(log_time: str) -> None:
    """处理指定日所有设备累积数据

    把每台设备每日最后一条记录抽取出来
    """

    equipment_list = equipment.get_all()

    for item in equipment_list:
        cum = get_day_last(item.device_serialnumber, log_time)
        if cum is not None:
            save_to_summary(cum)
            # print('date: %s, equipment: %s is extract and save' % (log_time, item.device_serialnumber))

    print('cumulative biz daily process finish')
