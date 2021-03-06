"""
定时任务调度
"""

import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from app import biz

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
    print("This time is: %s" % datetime.datetime.now())


def daily():
    """处理前一天累积值
    """
    print("start daily process, %s " % datetime.datetime.now())

    prev = datetime.date.today() - datetime.timedelta(days=1)

    log_time = prev.__format__("%Y-%m-%d")
    print("prev date is: %s" % log_time)

    # 处理累积值
    biz.cumulative.daily_process(log_time)

    # 处理节能率
    biz.energy.daily_process(log_time)

    # 处理周节能率
    if datetime.date.today().weekday() == 0:
        print("process week save.")
        biz.week_save.daily_process(
            datetime.date.today().__format__("%Y-%m-%d"))

    print("finish daily process, %s " % datetime.datetime.now())
    return


def start_job(hour: int, minute: int):
    """启动定时任务
    """
    scheduler.add_job(daily, "cron", id="timer", hour=hour, minute=minute)
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
