from celery.schedules import crontab

BROKER_URL = "redis://"
CELERY_RESULT_BACKEND = "db+sqlite:///results.db"

CELERYBEAT_SCHEDULE = {
    "ping-sln": {
        "task": "tasks.ping",
        "schedule": crontab(),
        "args": ("simcoe.science.uoit.ca",)
    },
    "ping-ext": {
        "task": "tasks.ping",
        "schedule": crontab(),
        "args": ("rdrake.org",)
    },
    "download-sln": {
        "task": "tasks.download",
        "schedule": crontab(minute="0,15,30,45"),
        "args": ("http://leda.science.uoit.ca:9001/data.bin",)
    },
    "download-ext": {
        "task": "tasks.download",
        "schedule": crontab(minute="1,16,31,46"),
        "args": ("http://rdrake.org:9001/data.bin",)
    }
}
