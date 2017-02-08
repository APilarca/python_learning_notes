import random

# list of words
words = [
'apple',
'banana',
'orange',
'coconut',
'strawberry',
'lemon',
'blueberry',
'melon'
]

while True:
	start = raw_input("Press enter/return to start or enter Q to quit")
	if start.lower() == 'q':
		break
# pick random word
	secret_word = random.choice(words)
	bad_guesses = []
	good_guesses = [ ]
# draw spaces
# take guess
# draw guessed letters and strikes
# print win/lose

