from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from twi import send_alert


sched = BlockingScheduler()
# Schedule job_function to be called every two hours
sched.add_job(send_alert, 'interval', seconds=10)
sched.start()