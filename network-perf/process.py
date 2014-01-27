import datetime, sqlite3, time

import matplotlib.dates as dates
import matplotlib.pyplot as plt

import pandas
import pandas.io.sql as psql

conn = sqlite3.connect("results.db", detect_types=sqlite3.PARSE_DECLTYPES)
conn.row_factory=sqlite3.Row

df = psql.read_frame("SELECT event_time, action, target, duration FROM entries", con=conn)#, index_col="event_time")

df.sort(["action", "target", "event_time"], inplace=True)

grouped = df.groupby(["action", "target"])

for (k, grp) in grouped:
    (action, target) = (k[0], k[1])

    if action == "PING":
        ylabel = "Latency"
    elif action == "DOWN":
        ylabel = "Duration"

    fig = plt.figure(action)

    ax = grp.plot(x="event_time", y="duration", label=target)

    ax.set_xlabel("Timestamp")
    ax.set_ylabel("{} (ms)".format(ylabel))
    ax.legend(loc="best")
    ax.xaxis.set_major_formatter(dates.DateFormatter("%b %d\n%H:%M:%S"))

plt.show()
