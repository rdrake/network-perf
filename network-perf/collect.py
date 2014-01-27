from celery import Celery

celery = Celery()
celery.config_from_object("celeryconfig")

if __name__ == "__main__":
    print("wuuuut")
    celery.start()

#from apscheduler.scheduler import Scheduler
#from apscheduler.jobstores.shelve_store import ShelveJobStore

from ping import Ping
from download import Download

import argparse, datetime, logging, socket, sqlite3

whoami = socket.getfqdn()

#logging.basicConfig(level=logging.DEBUG, format="%(levelname)s[%(asctime)s]: %(message)s")

parser = argparse.ArgumentParser(description="Collect network performance data.")
parser.add_argument("-n", "--count", type=int, default=5, help="number of IMCP packets to send")
parser.add_argument("-c", "--config", default="conf/config.ini", help="configuration file")
parser.add_argument("--result", required=True, help="location to store results in")
parser.add_argument("--ping", required=True, nargs="+", help="targets to ping")
parser.add_argument("--down", required=True, nargs="+", help="targets to download")

args = parser.parse_args()

#conn = sqlite3.connect(args.result, check_same_thread=False)
#cur = conn.cursor()

#cur.execute("DROP TABLE IF EXISTS entries");
#cur.execute("CREATE TABLE entries (event_time TIMESTAMP, action TEXT, source TEXT, target TEXT, duration FLOAT)")

#sched = Scheduler(standalone=True, coalesce=True)
#sched.add_jobstore(ShelveJobStore("jobs.shelve"), "file")

#def record_result(target, time_in_ms):
#    cur.execute("INSERT INTO entries VALUES (?, ?, ?, ?, ?)", (datetime.datetime.now(), "PING", whoami, target, str(time_in_ms)))
#    conn.commit()

#def ping(host):
#    p = Ping(args.count)
#    record_result(host, p.time(host))

#def download(url):
#    d = Download()
#    record_result(url, d.time(url))

#for target in args.ping:
#    sched.add_cron_job(ping, second="0,30", args=[target])

#for (i, target) in enumerate(args.down):
#    # Stagger downloads by 5 minutes (don't go over 60 seconds)
#    minute = int(i * 5 % 60)
#    sched.add_cron_job(download, minute=str(minute), args=[])

#sched.print_jobs()
#sched.start()
