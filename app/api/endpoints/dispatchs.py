from fastapi import APIRouter, Query
from app import biz
from datetime import datetime
import pytz

router = APIRouter()


@router.get("/start-job")
async def start_job(hour: int = Query(..., title="小时"),
                    minute: int = Query(..., title="分钟")):
    """启动定时任务
    """
    biz.dispatch.start_job(hour, minute)
    return {"message": "ok"}


@router.get("/get-time")
async def get_time():
    """获取服务器时间
    """

    tz = pytz.timezone('Asia/Shanghai')

    return {
        'nowtime': datetime.now(),
        'utctime': datetime.utcnow(),
        'localtime': datetime.now(tz)
    }
