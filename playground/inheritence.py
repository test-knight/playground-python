import datetime as dt


class Member:
    free_days = 30

    def __init__(self, username, fullname):
        self.username = username
        self.fullname = fullname
        self.date_joined = dt.date.today()
        # expiration date
        self.expiration_date = self.date_joined + dt.timedelta(days=self.free_days)
        self.secret_code = ''
    
    def get_expiry(self):
        print(f"{self.username} expires on {self.expiration_date}")
    
    def get_status(self):
        print("User is a Member")


class Admin(Member):

    # free_days = 30 * 3

    def __init__(self, username, fullname, secret_code):
        super().__init__(username, fullname)
        self.secret_code = secret_code
    
    def get_status(self):
        print("User is an Admin")

    @classmethod
    def set_free_days(cls, days):
        cls.free_days = days


class User(Member):
    def get_status(self):
        print("User is an User")


riaz = Admin("riazraffi", "Riaz Raffi", "PRESTO")
print(riaz.username, riaz.fullname, riaz.secret_code, riaz.free_days)
riaz.get_expiry()
riaz.get_status()
print()
fiaz = User("fiazraffi", "Fiaz Raffi")
print(fiaz.username, fiaz.fullname, fiaz.secret_code, fiaz.free_days)
print(fiaz.get_expiry())
fiaz.get_()