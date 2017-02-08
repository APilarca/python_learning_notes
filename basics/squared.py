def squared(arg):
	try:
		arg = int(arg)
	except ValueError:
		print(arg * len(arg))
	else:
		print(arg ** 2)

given = raw_input("What would you like to square?  ")

squared(given)
