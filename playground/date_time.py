import datetime as dt
from dateutil.tz import gettz

date_now = dt.date.today()
print(f"{date_now:Today %x is day %j of the year %Y %Z}")
date_any = dt.date(2021, 10, 2)
print(f"{date_any:%A, %B %d, %Y }")

time_now = dt.time()
almost_midnight = dt.time(23, 59, 59, 999999)
print(f"{time_now}")
print(f"{almost_midnight:%I:%M:%S and %f microseconds %P}")

simple_date = dt.date(2021, 10, 4)
duration = dt.timedelta(days=276)
print(simple_date - duration)

right_now = dt.datetime.now()
print(f"Local: {right_now:%D %I:%M %p} {right_now.astimezone().tzinfo}")

birth_date = dt.datetime(1988, 12, 25, 2, 30)
print(right_now - birth_date)

eastern_time = right_now.astimezone(gettz('America/New_York'))
print(f"{eastern_time:%D %I:%M %p %Z}")

utc_time = right_now.astimezone(gettz('Etc/UTC'))
print(f"{utc_time:%D %I:%M %p %Z}")

ist_time = right_now.astimezone(gettz('Asia/Calcutta'))
print(f"{ist_time:%D %I:%M %p %Z}")