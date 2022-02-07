# defining a class
import datetime as dt

from platformdirs import user_runtime_dir

class Member:
    """Definition of a class Car"""

    free_days = 90

    def __init__(self, uname, fname):
        self.username = uname
        self.full_name = fname

        self.is_active = True
        self.datetime_joined = dt.date.today()

        self.free_trial_expiry = self.datetime_joined + dt.timedelta(days=self.free_days)

    def terminate(self):
        self.is_active = False

    def date_joined(self):
        return f"{self.full_name} joined on {self.datetime_joined:%m-%d-%y}"

    # class methods
    @classmethod
    def set_freedays(cls, days):
        cls.free_days = days

    # static methods
    @staticmethod
    def current_time():
        now = dt.datetime.now()
        return f"Current time is {now:%I:%M %p}"


user_1001 = Member('riaz', 'Riaz Raffi')
print(user_1001)
print(user_1001.username)
print(user_1001.full_name)
print(user_1001.is_active)
print(user_1001.datetime_joined)
print(type(user_1001))

user_1001.terminate()
print(user_1001.is_active)

print(user_1001.date_joined())

# Alternative format for calling a function with instance
print(Member.date_joined(user_1001))
# print(Member.date_joined(user_1002)) # in valid object)
print(user_1001.free_trial_expiry)
Member.free_days = 365
print(user_1001.free_trial_expiry)
user_1002 = Member('fiaz', 'Fiaz Raffi')
user_1002.set_freedays(30)
print(user_1002.free_trial_expiry)
print(Member.current_time())

