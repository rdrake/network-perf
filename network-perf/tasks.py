from ping import Ping
from download import Download

from collect import app

PING_COUNT = 5

@app.task
def ping(host):
    print("Executing ping")
    p = Ping(PING_COUNT)
    return (p.time(host), host)

@app.task
def download(url):
    d = Download(url)
    return (d.time(url), url)
