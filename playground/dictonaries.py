# declaring a dictionary
customer = {
    "name": "Riaz",
    "age": 32,
    "is_verified": True
}

# print a key value. Throws traceback if not found
print(customer["name"])

# prints a key value. Does not throw error if not present, instead displays a message.
print(customer.get("name_", "Not Valid"))


# program to print the phone number (in words)
phone = input("Phone Number:")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

words = ""

for ch in phone:
    words += digits_mapping.get(ch, "!") + " "

print(words)
