
text = input("Enter a string: ")

count = 0


for ch in text:
    if ch.lower() in "aeiou":
        count = count + 1

print("Number of vowels =", count)