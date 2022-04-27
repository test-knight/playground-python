f = open('quotes.txt')
print(f.read())

print("Is file closed? ", f.closed)

f.close()

# contextual blocks, automatically closes the file 
with open('quotes.txt') as f:
    print(f.read())

print("Is file closed? ", f.closed)

# binary file reading
with open('/Users/rraffi/Downloads/happy_pickle.jpg', 'rb') as f:
    print(f.read())
print()

with open('quotes.txt') as f:
    for index, line in enumerate(f.readlines()): 
        if index % 2 == 0:
            print(line, end='')
        else:
            print(' ', line)


# reading one line at a time
with open('quotes.txt') as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()

# writing to a file and then reading
name = "Riaz Raffi"

with open('quotes.txt', 'a') as f:
    f.write(str('by' + name + '\n'))

print('\nDone')

with open('quotes.txt') as f:
    print(f.read())
