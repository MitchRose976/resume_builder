import sched
import time
import subprocess
from assets.get_new_proxies import get_new_proxies

def run_proxy_jobs():
    subprocess.run(['python', 'assets/get_new_proxies.py'])
    subprocess.run(['python', './check_proxies.py'])
    subprocess.run(['python', './test_proxies.py'])

scheduler = sched.scheduler(time.time, time.sleep)

def run_scripts_every_hour(sc):
    run_proxy_jobs()
    scheduler.enter(3600, 1, run_scripts_every_hour, (sc,))

scheduler.enter(0, 1, run_scripts_every_hour, (scheduler,))

scheduler.run()
