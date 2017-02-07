import random

def game():
	# generate ran num from 1 - 10
	secret_num = random.randint(1, 10)
	guesses = []

	def add_guess(guessed):
		guesses.append(guessed)
	# get guess
	while len(guesses) < 5:
		try:
			guess = int(input("Guess a number between 1 and 10: "))
		except ValueError:
			print("{} isn't a number, try again!".format(guess))
		else:
			if guess == secret_num:
				print("You got it! My number was {}".format(secret_num))
				break
			elif guess > secret_num:
				print("Sorry too hi!")
				add_guess(guess)
			else:
				print("Too low!")
				add_guess(guess)
		# print hit/miss

game()