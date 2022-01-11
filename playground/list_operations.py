letters = ['B','A','C','D','C','E','F','L','G','E','C','K']

print(letters)

print(len(letters))

letters.append('Z')
print(letters)

letters.insert(7, 'I')
print(letters)

letters.remove('K')
print(letters)

while 'C' in letters:
    letters.remove('C')
print(letters)

letters_new = ['Q','R','V']
letters.extend(letters_new)
print(letters)

letter_first = letters.pop(0)
letter_last = letters.pop()
print(letters)
print(f'Removed letters {letter_first} & {letter_last}')

del letters[9]
print(letters)

# del letters // deletes the whole list
# print(letters)

# letters.clear() // clears the whole list
# print(letters)

print(letters.count('E'), letters.count('C'))
print(letters.count('V'))
print(letters.index('E'))
# print(letters.index('C')) # throws error if not found

letters.sort()
print(letters)

# copying a list passes reference to the list. So use 'copy()`
list_one = ['B', 'A', 'C', 'D', 'C', 'E', 'F', 'L', 'G', 'E', 'C', 'K'] 
list_two = list_one.copy()
list_one.reverse() #reverse list_one
print(list_two) #list_two remains unmodifed
