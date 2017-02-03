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

# for and while loops

my_list = ['hello', 'how', 'are', 'you']

for word in my_list:
	print(word.upper())

for num in [1, 2, 3, 4]:
	if num % 2 == 0:
		print(num)

start = 10
while start:
	print(start)
	start -= 1

names = ['Angelica', 'Geezer', 'QUIT', 'Kug']

for name in names:
	if name == 'QUIT':
		break
	print(name)

# using input

age =  int(input("What's your age? "))
print(age + 1)

# writing functions

