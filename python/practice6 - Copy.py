Word = input("Enter A Word:")
count=0
for char in Word:
    if char in "aeiouAEIOU":
        count = count + 1
print("Number of vowels =", count)