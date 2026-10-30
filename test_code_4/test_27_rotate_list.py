import importlib

rotate_mod = importlib.import_module("27_rotate_list")
rotate_list = rotate_mod.rotate_list

def test_rotate_basic():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotate_zero():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]

def test_rotate_larger_k():
    assert rotate_list([1, 2, 3], 4) == [3, 1, 2]

def test_rotate_empty():
    assert rotate_list([], 2) == []
