import socket

from celery import Celery

from ping import Ping
from download import Download

PING_COUNT = 5

whoami = socket.getfqdn()

app = Celery("tasks")
app.config_from_object("celeryconfig")

@app.task
def ping(host):
    p = Ping(PING_COUNT)
    return (p.time(host), whoami, host)

@app.task
def download(url):
    d = Download(url)
    return (d.time(url), whoami, url)
