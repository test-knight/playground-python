def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 1


print(greet(1), 'Riaz')

sval = 1.0
print(type(sval))

def sayHello(name):
    """ Prints a hello with your first name"""
    print(f'Hi there, {name}!')
    print(f'{name}, you are welcome aboard')


sayHello("Riaz")
sayHello("Fiaz")

def square(number) -> bool:
    return number * number


print(square(3))
