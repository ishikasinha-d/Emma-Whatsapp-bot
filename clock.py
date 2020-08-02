from apscheduler.schedulers.blocking import BlockingScheduler
from app import send
s=BlockingScheduler()
s.add_job(send,'interval',seconds=10)
s.start()

