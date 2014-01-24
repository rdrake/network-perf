import datetime, sqlite3, time

from matplotlib import pyplot as plt
import matplotlib

#from thrush import rrd
#
#RRD_FILE = "results.rrd"

conn = sqlite3.connect("results.db", detect_types=sqlite3.PARSE_DECLTYPES)
conn.row_factory=sqlite3.Row
cur = conn.cursor()

#class SLNRRD(rrd.RRD):
#    duration = rrd.Gauge(heartbeat=60)
#
#slnrrd = SLNRRD(RRD_FILE)
#
#if not slnrrd.exists():
#    slnrrd.create()

datetimes = []
values = []

for row in cur.execute("SELECT event_time, action, target, duration FROM entries"):
    if row["action"] == "DOWN" and row["target"] == "http://rdrake.org:9001/data.bin":
        datetimes.append(row["event_time"])
        values.append(row["duration"])

dates = matplotlib.dates.date2num(datetimes)
plt.plot_date(dates, values, xdate=True, ls="-")
plt.xlabel("Time")
plt.ylabel("Latency (ms)")
plt.show()
    #slnrrd.update(time.mktime(row["event_time"].timetuple()), duration=row["duration"])
