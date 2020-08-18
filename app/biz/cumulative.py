'''
累积数据操作业务
'''

from pymongo import MongoClient
from app.models.cumulative import Cumulative


def get_day_first(serial_number: str) -> Cumulative:
    '''
    获取当日第一条记录
    '''
    client = MongoClient('mongodb://admin:Molan%402019@118.31.35.17:27017/')
    db = client.get_database('water_heater')
    collection = db.get_collection('equipment_cumulative')
    fil = {
        'device_serialnumber': serial_number,
        'log_time': {
            '$gte': '2020-07-01 00:00:00'
        }
    }
    sort = [('log_time', -1)]
    data = collection.find_one(fil, sort=sort)

    if data is None:
        return None
    else:
        cum = Cumulative(**data)
        return cum
