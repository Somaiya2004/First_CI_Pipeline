import importlib

anagram_mod = importlib.import_module("22_anagram_strings")
are_anagrams = anagram_mod.are_anagrams

def test_anagrams_true():
    assert are_anagrams("listen", "silent") == True

def test_anagrams_false():
    assert are_anagrams("hello", "world") == False
