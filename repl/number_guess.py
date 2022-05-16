import random

print("Hello, what is your name?")
name = input()
print('Hello, ' + name)
secret_number = random.randint(1,10)

for guess_taken in range(1, 7):
	number = int(input("Guess a number: "))

	if number > secret_number:
		print("Your guess is higher")
	elif number < secret_number:
		print("Your guess is lower")
	elif number == secret_number:
		print(number, " is correct.")
		print("You guessed in " + str(guess_taken) + " guesses.")
		break

	if guess_taken == 6:
		print("Sorry. The number that I was thinking of was " + str(secret_number))


