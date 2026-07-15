from text_analytics import word_count, unique_words, reverse_text

def test_word_count():
    text = "hello world hello"
    assert word_count(text) == {"hello": 2, "world": 1}

def test_unique_words():
    text = "hello world hello"
    assert unique_words(text) == {"hello", "world"}

def test_reverse_text():
    text = "hello"
    assert reverse_text(text) == "olleh"

def test_empty_string():
    text = ""
    assert word_count(text) == {}
    assert unique_words(text) == set()
    assert reverse_text(text) == ""

def test_single_word():
    text = "hello"
    assert word_count(text) == {"hello": 1}
    assert unique_words(text) == {"hello"}
    assert reverse_text(text) == "olleh"

def test_special_characters():
    text = "hello, world! hello."
    assert word_count(text) == {"hello,": 1, "world!": 1, "hello.": 1}
    assert unique_words(text) == {"hello,", "world!", "hello."}
    assert reverse_text(text) == ".olleh !dlrow ,olleh"

def test_case_sensitivity():
    text = "Hello hello"
    assert word_count(text) == {"Hello": 1, "hello": 1}
    assert unique_words(text) == {"Hello", "hello"}
    assert reverse_text(text) == "olleh olleH"