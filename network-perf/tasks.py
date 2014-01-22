from apscheduler.scheduler import Scheduler
from apscheduler.jobstores.shelve_store import ShelveJobStore

from ping import Ping
from download import Download

import datetime, logging, sqlite3

logging.basicConfig(level=logging.DEBUG,
        format='%(levelname)s[%(asctime)s]: %(message)s')
#logging.getLogger().addHandler(logging.StreamHandler())

PING_COUNT = 5

conn = sqlite3.connect("results.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS entries");
cur.execute("CREATE TABLE entries (timestamp DATE, action TEXT, target TEXT, duration FLOAT)")

sched = Scheduler(standalone=True, coalesce=True)
sched.add_jobstore(ShelveJobStore("jobs.shelve"), "file")

def ping(host):
    p = Ping(PING_COUNT)
    t = p.time(host)
    cur.execute("INSERT INTO entries VALUES (?, ?, ?, ?)", (datetime.datetime.now(), "PING", host, str(t)))
    conn.commit()

def download(url):
    d = Download()
    t = d.time(url)
    cur.execute("INSERT INTO entries VALUES (?, ?, ?, ?)", (datetime.datetime.now(), "DOWN", url, str(t)))
    conn.commit()

sched.add_cron_job(ping, minute="*", second="30", args=["simcoe.science.uoit.ca"])
sched.add_cron_job(ping, minute="*", second="0", args=["rdrake.org"])

sched.add_cron_job(download, minute="0,30", args=["http://leda.science.uoit.ca:9001/data.bin"])
sched.add_cron_job(download, minute="5,35", args=["http://rdrake.org:9001/data.bin"])

sched.print_jobs()

sched.start()
