print(range(4))
print(list(range(4)))
print(list(range(0, 100, 2)))

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

for i in range(len(supplies)):
    print("Item in index " + str(i) + " of supplies is: " + supplies[i])