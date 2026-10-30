import importlib

max_min_mod = importlib.import_module("25_max_min_list")
find_max_min = max_min_mod.find_max_min

def test_max_min_basic():
    assert find_max_min([3, 1, 4, 1, 5, 9, 2, 6]) == (9, 1)

def test_max_min_negative():
    assert find_max_min([-5, -1, -10, -3]) == (-1, -10)

def test_max_min_single():
    assert find_max_min([42]) == (42, 42)

def test_max_min_empty():
    assert find_max_min([]) == (None, None)
