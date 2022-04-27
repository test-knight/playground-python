# try:
#     age = int(input("> "))
#     print("Ages is", age)
#     income = 20000
#     risk = income/age
# except ZeroDivisionError:
#     print("Age cannot be 0.")
# except ValueError:
#     print("Invalid number entry")


try:
    file = open("imdb_movie_list_scraped.csv")
    print(file.name)
    print('\n\n', file.readline())
    # print(file.some_random_method())
    # raise Exception("What?")
except FileNotFoundError:
    print("Sorry, file not found")
except Exception as e:
    print(e)
else:
    print("Shows this if there is not exception")
finally:
    print("This is in the finally block")
