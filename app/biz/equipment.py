"""
设备操作业务
"""

from app.models.equipment import Equipment
from app.db import water_heater
from typing import List


def get_all() -> List[Equipment]:
    """获取所有设备
    """
    data: List[Equipment] = []

    collection = water_heater.get_equipment()

    for item in collection.find():
        equip = Equipment(**item)
        data.append(equip)

    return data
