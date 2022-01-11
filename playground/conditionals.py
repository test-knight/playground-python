x = 100

# nested if
if x > 2:
    print("Bigger than 2")
    if x > 50:
        print("Bigger than 50")
print('Done with 2')

# conditional if
if x < 2:
    print('Less than 2')
elif x < 10:
    print('Less than 10')
elif x < 50:
    print("Less than 50")
else:
    print("Nothing to match")

# try/except error handling

inStr = input("Enter a number:")

try:
    iVal = int(inStr)
except:
    iVal = -1

if iVal > 0:
    print('Good')
else:
    print('Not a number')