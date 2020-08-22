from fastapi import APIRouter, Query
from app import biz

router = APIRouter()


@router.get("/start-job")
async def start_job(hour: int = Query(..., title="小时"),
                    minute: int = Query(..., title="分钟")):
    """启动定时任务
    """
    biz.dispatch.start_job(hour, minute)
    return {"message": "ok"}
