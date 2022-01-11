file_name = input()

try:
    file_handle = open(file_name)
except:
    print("File not found", file_name)
    quit()

# for line in file_handle:
#     if not line.startswith(' '):
#         print(line)

reader = file_handle.read()
print(reader)
