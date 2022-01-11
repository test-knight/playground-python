def hello(fname="nobody"):
    print("Hello " + fname)


hello("Riaz")
hello()


def sign_in(fname, date, lname="unknown"):
    msg = "Hello "
    if lname != "unknown":
        msg += fname + " " + lname + " " f"Signed in on {date}"
    else:
        msg += fname + " " f"Signed in on {date}"
    print(msg)


sign_in("Riaz", "12/25/1988", "Raffi")
sign_in("Riaz", "12/25/1988")
sign_in(date="10/02/1987", lname="Polattie", fname="Sarah")