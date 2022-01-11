# defining a class
import datetime as dt

class Member:
    """Definition of a class Car"""

    def __init__(self, uname, fname):
        self.username = uname
        self.full_name = fname

        self.is_active = True
        self.datetime_joined = dt.date.today()

    def terminate(self):
        self.is_active = False


user_1001 = Member('riaz', 'Riaz Raffi')
print(user_1001)
print(user_1001.username)
print(user_1001.full_name)
print(user_1001.is_active)
print(user_1001.datetime_joined)
print(type(user_1001))
user_1001.terminate()
print(user_1001.is_active)
