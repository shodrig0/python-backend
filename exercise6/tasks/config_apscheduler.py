from apscheduler.schedulers.background import BackgroundScheduler
from tasks.run_random_price import run_random_price

scheluder = BackgroundScheduler()

scheluder.add_job(run_random_price, "interval", minutes = 1)

# scheluder.start()