class EmptyFileException(Exception):
    pass


try:
    file = open("countries_population_list_1.csv")
    print(file.name)
    if len(file.readlines()) < 1:
        raise EmptyFileException("Test")
    file.seek(0)
    if len(file.readlines()) < 2:
        raise Exception("Only header present")
except FileNotFoundError as e:
    print("Sorry, that file could not be found")
except EmptyFileException:
    print("Sorry, file is empty" + str(e))
except Exception as e:
    print("\n\n Something went wrong: " + str(e))
