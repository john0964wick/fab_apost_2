from apscheduler.schedulers.blocking import BlockingScheduler
from main import full_pipeline

if __name__ == "__main__":
    sched = BlockingScheduler()
    sched.add_job(full_pipeline, 'interval', hours=4)
    sched.start()
