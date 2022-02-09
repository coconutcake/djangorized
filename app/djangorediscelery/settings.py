CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_IMPORTS = ['djangorediscelery.tasks',]
from celery.schedules import crontab

# CRON tasks here -------------------------------

# CELERY_BEAT_SCHEDULE = {
#     'printHello': {
#         'task': 'djangorediscelery.tasks.printHello',
#         'schedule': 10.0,
#     },
# }