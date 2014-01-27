from celery import Celery
from celery.schedules import crontab

app = Celery("network-perf.collect", broker="redis://", backend="db+sqlite:///results.db", include=["network-perf.tasks"])

CELERYBEAT_SCHEDULE = {
    "ping-sln": {
        "task": "tasks.ping",
        "schedule": crontab(),
        "args": "simcoe.science.uoit.ca"
    },
    "ping-ext": {
        "task": "tasks.ping",
        "schedule": crontab(),
        "args": "rdrake.org"
    },
    "download-sln": {
        "task": "tasks.download",
        "schedule": crontab(minute="0,30"),
        "args": "http://leda.science.uoit.ca:9001/data.bin"
    },
    "download-ext": {
        "task": "tasks.download",
        "schedule": crontab(minute="1,31"),
        "args": "http://rdrake.org:9001/data.bin"
    }
}

if __name__ == "__main__":
    app.start()
