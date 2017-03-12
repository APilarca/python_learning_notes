sodas = ['Pepsi', 'Cherry Coke', 'Sprite']
chips = ['Dorritos', 'Fritos']
candy = ['Snickers', 'Twizzlers']

while True:
	choice = raw_input("Would you like SODA, CHIPS, or CANDY? ").lower()
	try:
		if choice == 'soda':
			snack = sodas.pop()
		elif choice == 'chips':
			snack = chips.pop()
		elif choice == 'candy':
			choice = candy.pop()
		else:
			print("Sorry, I didn't understand that.")
			continue
	except IndexError:
		print("We're all out of {}! Sorry!".format(choice))
	else:
		print("Here's your {} : {}". format(choice, snack))