n = 1
while n > 0:
    print("Riaz")
    n -= 1

print("Raffi")

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    elif line == 'stop':
        break
    else:
        print("Printing", line)


print("Done!")
