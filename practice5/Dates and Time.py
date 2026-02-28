import datetime
now = datetime.datetime.now()
print(now)


d = datetime.date(2026, 2, 28)
t = datetime.time(14, 30, 15)
print("Date:", d)
print("Time:", t)


from datetime import date
today = date.today()
print(today)


now = datetime.now()
print(now.strftime("%Y-%m-%d"))


now = datetime.now()
print(now.strftime("%A, %B %d, %Y"))


now = datetime.now()
print(now.strftime("%H:%M:%S"))


d1 = date(2026, 2, 28)
d2 = date(2026, 3, 5)
delta = d2 - d1
print(delta.days)


from datetime import datetime
import pytz
tz_ny = pytz.timezone("America/New_York")
now_ny = datetime.now(tz_ny)
print(now_ny)