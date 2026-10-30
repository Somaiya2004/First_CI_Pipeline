import importlib

largest_word_mod = importlib.import_module("21_largest_word")
largest_word = largest_word_mod.largest_word

def test_largest_word_basic():
    assert largest_word("Python is an amazing programming language") == "programming"

def test_largest_word_single():
    assert largest_word("hello") == "hello"

def test_largest_word_empty():
    assert largest_word("") == ""
