class Errors(Exception):
    pass


class EmptyFileError(Errors):
    pass


try:
    file = open('imdb_movie_list_scraped.csv')

    file_content = file.readlines()
    file_length = len(file_content)

    if file_length < 2:
        raise EmptyFileError

except FileNotFoundError:
    print("File was not found")
except EmptyFileError:
    print("Not enough stuff to read")
    file.close()
except Exception as e:
    print("\n\n\ Failed: The error: " + str(e))
    file.close()
else:
    print('No exceptions were throw')
    print(file)
    for line in file_content:
        print(line)

    file.close()
