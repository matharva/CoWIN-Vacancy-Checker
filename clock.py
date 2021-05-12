print("Hello World")
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from twi import send_alert


print("Hello World")
sched = BlockingScheduler()
print(sched)
print("Hello World")
# Schedule job_function to be called every two hours
sched.add_job(send_alert, 'interval', seconds=10)
print("Hello World")
sched.start()