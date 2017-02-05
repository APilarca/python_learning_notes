import random

# generate ran num from 1 - 10
secret_num = random.randint(1, 10)
# get guess

while True:
	guess = int(input("Guess a number between 1 and 10: "))
	if guess == secret_num:
		print("You got it! My number was {}".format(secret_num))
		break
	elif guess > secret_num:
		print("Sorry too hi!")
	else:
		print("Try lower!")
# print hit/miss

