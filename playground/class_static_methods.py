import datetime as dt


class Member:
    free_days = 30

    def __init__(self, username, fullname):
        self.date_joined = dt.date.today()
        # expiration date
        self.expiration_date = self.date_joined + dt.timedelta(days=self.free_days)

    def when(self):
        print(str(dt.time()))


    @classmethod
    def time_now(cls):
        print(dt.datetime.now())

    @staticmethod
    def today():
        print(dt.date.today())


print("Member Methods")
rraffi = Member('rraffi', "Riaz Raffi")
print(rraffi.free_days)
print(Member.free_days)
print(rraffi.date_joined)
print(rraffi.expiration_date)
rraffi.when()
# Member.when()

# changing class variables on the fly
Member.free_days = 90
print(f"For rraffi {rraffi.free_days}")

fraffi = Member('rraffi', "Riaz Raffi")
print(fraffi.free_days)
print(Member.free_days)
print(fraffi.date_joined)
print(fraffi.expiration_date)

print("Class Method")
Member.time_now()
rraffi.time_now()

print("Static Method")
Member.today()
rraffi.today()

