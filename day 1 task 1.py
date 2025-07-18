def count_vowels(text):
    vowels = "aeiou"
    text = text.lower()
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text = "hello my name is Ahmed, iam student at iti"
print("Number of vowels:", count_vowels(text))