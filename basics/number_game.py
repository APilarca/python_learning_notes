import random

def game():
	# generate ran num from 1 - 10
	secret_num = random.randint(1, 10)
	guesses = []

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
			else:
				print("Too low!")
		guesses.append(guess)

	else:
		print("You didn't get it! My number was {}".format(secret_num))
	play_again = raw_input("Would you like to play again? (Y/n)  ")
	if play_again.lower() != 'n':
		game()
	else:
		print("Thanks for playing!")

game()