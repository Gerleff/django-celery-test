from celery import Celery
from celery.schedules import crontab

from .settings import TIME_ZONE
from .wsgi import *
from api.models import Account


app = Celery('backoffice', broker='redis://redis:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
def hold_handler():
    for account in Account.objects.filter(hold__gt=0):
        if account.balance >= account.hold:
            account.balance -= account.hold
            account.hold = 0
            account.save()
            print(f'Account\'s UUID: {account.id}\n HOLD --> BALANCE performed.\n')


app.conf.beat_schedule = {
    'hold_to_balance': {
        'task': 'backoffice.celery.hold_handler',
        'schedule': crontab(minute='*/10')
    }
}
app.conf.timezone = TIME_ZONE

