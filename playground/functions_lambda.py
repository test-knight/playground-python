names_two = ['Adam', 'Zaire', 'diMoela', 'Ram']
names_three = names_two.copy()
names_three.sort()
print(names_three)

def lowercaseof(anystring):
    return anystring.lower()

names_four = names_two.copy()
names_four.sort(key=lowercaseof)
print(names_four)

# same expression as above can be represented as lambda (anonymous function)
names_five = names_two.copy()
names_five.sort(key=lambda s: s.lower())
print(names_five)

currency = lambda n: f"${n:,.2f}"
percentage = lambda n: f"{n:.2%}"
print(currency(4500))
print(percentage(0.45))