def max_of(array):
    largest_so_far = -1
    for num in array:
        if num > largest_so_far:
            largest_so_far = num
        print(largest_so_far, num)
    print("Done! The largest is", largest_so_far)


array = [9, 75, 20, 3, 74, 11]
print(max_of(array))

print(len(array))

total = 0
count = 0
for number in [112, 15, 10]:
    total = total + number
    count += 1

print(type(total/count))

# None data type. Finding the smallest number.
smallest = None
for value in [9, 10, 1, 13, 27, 0]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)

print("Done! Smallest number is", smallest)
