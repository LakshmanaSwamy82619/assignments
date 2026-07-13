def find_longest_word(sentence):
    # This function finds and returns the longest word in a sentence.
    words = sentence.split()  # Split the sentence into words using whitespace.

    # Start with an empty string so that the first word will become the longest.
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