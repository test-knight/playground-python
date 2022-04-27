import datetime

names = ['Zara', 'Lupe', 'Hong', 'Alberto', 'Jake', 'Tyler', 'riaz']
names_reverse = names.copy()
names_reverse.reverse()

numbers = [14, 0, 56, -4, 99, 11.23]

date_list = []
date_list.append(datetime.date(2020, 12, 31))
date_list.append(datetime.date(2019, 1, 31))
date_list.append(datetime.date(2018, 2, 28))
date_list.append(datetime.date(2020, 1, 1))

# names.sort()
# numbers.sort()
# date_list.sort()

names.sort(reverse=True)
numbers.sort(reverse=True)
date_list.sort(reverse=True)

print(names)
print(names_reverse)
print(numbers)

for date in date_list:
    print(f'{date:%m/%d/%Y}')
