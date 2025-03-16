# Count vowels in a word
word = input("Enter a word: ").lower()
vowels = "aeiou"
count = sum(1 for char in word if char in vowels)

print(f"Number of vowels: {count}")
