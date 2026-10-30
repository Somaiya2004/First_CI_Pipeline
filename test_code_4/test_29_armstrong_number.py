import importlib

armstrong_mod = importlib.import_module("29_armstrong_number")
is_armstrong = armstrong_mod.is_armstrong

def test_armstrong_true():
    assert is_armstrong(153) == True
    assert is_armstrong(1634) == True

def test_armstrong_false():
    assert is_armstrong(123) == False

def test_armstrong_single_digit():
    assert is_armstrong(5) == True

def test_armstrong_negative():
    assert is_armstrong(-153) == False
