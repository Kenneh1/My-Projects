# Check if a word is a palindrome or not

word = input("Enter a word: ").lower()
if word == word[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
