# checking for things inside list using in keyword

days_open = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
today = 'Tuesday'

if today in days_open:
	print('Come on in!')

today = 'Saturday'

if today in days_open:
	print('Come on in!')
else:
	print("Sorry we're closed")

# can also use not in statement

if today not in days_open:
	print("Sorry we're closed")
