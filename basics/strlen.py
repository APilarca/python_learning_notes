given_word = raw_input("Enter a word  ")

def just_right(word):
    if len(word) < 5:
        print("Your string is too short")
    elif len(word) > 5:
        print("Your string is too long")
    else:
        return True

just_right(given_word)