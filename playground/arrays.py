# largest = None
# smallest = None
# array = []
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     try:
#         array.append(int(num))
#     except:
#         print("Invalid input")
#         continue
#
# for i in array:
#     if largest is None:
#         largest = i
#         smallest = i
#     elif i > largest:
#         largest = i
#     elif i < smallest:
#         smallest = i
#
# # for j in array:
# #     if smallest is None:
# #         smallest = j
# #     elif j < smallest:
# #         smallest = j
#
# print(array)
# print("Maximum is", largest)
# print("Minimum is", smallest)

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        sval = int(num)
        if largest is None or smallest is None:
            largest = sval
            smallest = sval
        elif sval > largest:
            largest = sval
        elif sval < smallest:
            smallest = sval
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)