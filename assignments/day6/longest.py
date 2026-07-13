def find_longest_word(sentence):
    words = sentence.split()  # Split the sentence into words using whitespace.
    longest_word = ""

    # Check each word and compare its length.
    for word in words:
        # If current word is longer than the stored longest word, update it.
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word  # Return the longest word found.

sentence = input("Enter a sentence: ")
longest = find_longest_word(sentence)
print("Longest word:", longest)
