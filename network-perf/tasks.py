import socket

from ping import Ping
from download import Download

# Putting settings here despite hating doing so
PING_COUNT = 5

PING_TARGETS = ["simcoe.science.uoit.ca", "rdrake.org"]
DOWNLOAD_TARGETS = ["http://leda.science.uoit.ca:9001/data.bin", "http://rdrake.org:9001/data.bin"]

whoami = socket.getfqdn()

app = Celery(broker="redis://", backend="db+sqlite:///results.db")

@app.task
def ping(host):
    p = Ping(PING_COUNT)
    return (p.time(host), host)

@app.task
def download(url):
    d = Download(url)
    return (d.time(url), url)
