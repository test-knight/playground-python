fname = input("File name: ")
try:
    fhand = open(fname)
except:
    print('File not found name', fname)
    quit()
print(fhand)

# count = 0
# #counting lines in a file
# for line in fhand:
#     count += 1
#
# print("Lines =", count)

#reading from the file
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

count = 0
# reading from a file with 'start' string
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject'):
        print(line)
        count += 1

print('There were', count, 'subject lines in', fname)


