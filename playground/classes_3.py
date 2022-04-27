import datetime as dt

today = dt.datetime.now().astimezone()

print(today)
today_formatted = f"Today is {today:%m %b %y %H:%M:%S %Z}"
print(today_formatted)
