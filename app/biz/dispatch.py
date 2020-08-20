"""
定时任务调度
"""

from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

jobstores = {"default": MemoryJobStore()}

executors = {
    "default": ThreadPoolExecutor(10),
    "processpool": ProcessPoolExecutor(5)
}

job_defaults = {"coalesce": False, "max_instances": 3}

# 后台任务
scheduler = BackgroundScheduler(jobstores=jobstores,
                                executors=executors,
                                job_defaults=job_defaults)


def tick():
    print("This time is: %s" % datetime.now())


def start_job():
    """启动定时任务
    """
    scheduler.add_job(tick, "cron", id="timer", hour=20, minute=4)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("job stop")
        pass


def stop_job():
    """停止定时任务
    """
    scheduler.shutdown(wait=False)
    scheduler.remove_job("timer")
