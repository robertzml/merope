from pymongo import MongoClient

connection_string = 'mongodb://admin:Molan%402019@118.31.35.17:27017/'
database = 'water_heater'


def get_equipment():
    """获取设备表
    """
    client = MongoClient(connection_string)
    db = client.get_database(database)
    collection = db.get_collection('equipment')
    return collection


def get_cumulative_collection():
    """获取设备累积数据表
    """
    client = MongoClient(connection_string)
    db = client.get_database(database)
    collection = db.get_collection('equipment_cumulative')
    return collection


def get_summary_cumulative():
    """获取汇总每日设备累积数据表
    """
    client = MongoClient(connection_string)
    db = client.get_database(database)
    collection = db.get_collection('summary_cumulative')
    return collection


def get_summary_save():
    """获取节能率表
    """
    client = MongoClient(connection_string)
    db = client.get_database(database)
    collection = db.get_collection('summary_save')
    return collection


def get_summary_week_save():
    """获取周节能率表
    """
    client = MongoClient(connection_string)
    db = client.get_database(database)
    collection = db.get_collection('summary_week_save')
    return collection
