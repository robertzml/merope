from pymongo import MongoClient


def get_cumulative_collection():
    """获取设备累积数据表
    """
    client = MongoClient('mongodb://admin:Molan%402019@118.31.35.17:27017/')
    db = client.get_database('water_heater')
    collection = db.get_collection('equipment_cumulative')
    return collection
