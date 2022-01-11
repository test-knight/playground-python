#list manipulation

# array as lists
friends = ['Riaz', 'John', 'Rahul']
print(len(friends))
print(range(len(friends)))

for i in range(len(friends)):
    print(i, friends[i])

x = list()
# printing array dir functions
print(dir(x))

# creating a list using constructor
items = list()
items.append("Riaz")
items.append("32")
print(items)
items.append("32.3")
print(items)
items.remove("Riaz")
print('Removed', items)

# finding items in a loop
print("Riaz" in items)

# lists are sortable and hence mutable. All elements in a list should be of same type
items.sort()
print(items)

numlist = list()
# while True:
#     inp = input("Enter number: ")
#     if inp == 'done' : break
#     numlist.append(float(inp))
#
# print('Average:', sum(numlist)/len(numlist))

spaceName = 'Riaz Mohammed Raffi'
commaName = 'Riaz, Mohammed, Raffi'
print(spaceName.split())
print(commaName.split(', '))

list_students = ['Riaz', 'Fiaz', 'Sarah', 'Larry']
is_ram = "Riaz" in list_students
print(is_ram)

