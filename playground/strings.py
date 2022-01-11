name = "Riazr"
print(name.upper())
print(name[1])
print(len(name))
# slicing of strings
print(name[1:])
# name[0] = "Fiaz"

index = 0
while index < len(name):
    letter = name[index]
    print(index, letter)
    index = index + 1

count_letter = 0
for letter in name.lower():
    if letter == 'r':
        count_letter = count_letter + 1

print('Found times', count_letter)
print('R' in name)

position = name.lower().find('a')
# returns -1 if not found
print(position)

string = "            Riaz Mohammed Raffi  "
print(string.strip())

# reading from a line of text
emailHeader = "from: riazmr@sctce.ac.in 20210104 1913 P"
newEmailHeader = emailHeader.replace('sctce', 'cet')
print(newEmailHeader)
atpos = emailHeader.find('@')
print(atpos)
spos = emailHeader.find(' ', atpos)
print(spos)
print(emailHeader[atpos + 1: spos])
print(type(emailHeader))
print(dir(emailHeader))
print(newEmailHeader)

# format operator
print('%s had scored a total of %g with an average of %d' % ('Riaz', 100.10, 10))
name_input = input("What is your name? >>")
print("My name is %s" % name_input)
