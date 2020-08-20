from fastapi import APIRouter
from app import biz

router = APIRouter()


@router.get("/start-job")
async def start_job():
    """启动定时任务
    """
    biz.dispatch.start_job()
    return {"message": "ok"}
