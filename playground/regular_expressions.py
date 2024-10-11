import re
file = open('mbox-short.txt')


for line in file:
    if re.search('^X-\S+:', line):
        print(line)
