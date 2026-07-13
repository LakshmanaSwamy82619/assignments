def count_vowels(text):
    vowels = "aeiou"
    count = 0

    # count vowels ignoring case
    for ch in text:
        if ch.lower() in vowels:
            count += 1

    return count


sentence = input("Enter a String: ")
result = count_vowels(sentence)
print("Number of vowels:", result)

