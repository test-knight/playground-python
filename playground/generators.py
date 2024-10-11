def greeting():
    print("Hi")
    yield 1
    print("How are you?")
    yield 2
    print("Are you there?")
    yield 3


messages = greeting()

result = next(messages)
print(result)

result = next(messages)
print(result)