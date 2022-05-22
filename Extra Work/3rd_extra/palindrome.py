word = input("Enter your Word: ")

for e in range(word.__len__()):
    if word[e-1] == word[-e]:
        pass
    else:
        print(f"The Word \"{word}\" is NOT a Palindrome!")
        exit()

print(f"The Word \"{word}\" is a Palindrome!")
