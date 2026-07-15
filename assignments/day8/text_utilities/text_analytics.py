from collections import Counter

def word_count(text):
    return Counter(text.split())

def unique_words(text):
    return set(text.split())

def reverse_text(text):
    return text[::-1]