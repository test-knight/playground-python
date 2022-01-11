import datetime as dt
from dateutil.tz import gettz

right_now = dt.datetime.now()
print(f'{right_now: Today is %A, %B %d, %Y %I:%M %p} {right_now.astimezone().tzinfo}')
pst_time = right_now.astimezone(gettz('America/Los_Angeles'))
utc_time = right_now.astimezone(gettz('Etc/UTC'))
ist_time = right_now.astimezone(gettz('Asia/Calcutta'))

def get_time_with_timezone(time_zone: str, date_time: dt):
    print(f'Time in {time_zone.upper()} is {date_time:%A, %B %d %I:%M %p %Z}')

get_time_with_timezone('greenwich', utc_time)
get_time_with_timezone('pacific', pst_time)
get_time_with_timezone('india', ist_time)
