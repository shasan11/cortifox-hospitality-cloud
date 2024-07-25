import contextlib
from apscheduler.schedulers.background import BackgroundScheduler 
from django_apscheduler.jobstores import DjangoJobStore,register_events
from django.core.management import call_command

def db_backup():
    call_command("dbbackup")

def start():
        scheduler=BackgroundScheduler()
        scheduler.add_jobstore(DjangoJobStore(),"default")  
        scheduler.add_job(db_backup,'interval',minutes=30,jobstore="default",id='half_hourly_backup',replace_existing=True)
        register_events(scheduler)
        print("Half Hourly Backup Started")
        scheduler.start
        