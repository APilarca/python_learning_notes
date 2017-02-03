shopping_list = []

print("What should we get at the store?")
print("Enter 'DONE' to stop adding items.")

# because i'm running an older version of python
# i'm using raw_input() instead of just input()

while True:
	new_item = raw_input("> ")
	if new_item == "DONE":
		break
	shopping_list.append(new_item)

print("Here's your list:")

for item in shopping_list:
	print(item)