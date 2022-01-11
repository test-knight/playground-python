try:
    age = int(input("> "))
    print("Ages is", age)
    income = 20000
    risk = income/age
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid number entry")
