words = ["apple", "banana", "orange", "umbrella", "grape", "elephant", "kiwi"]

vowels = "aeiou"

res = [word for word in words if word[0].lower() in vowels]

print(res)