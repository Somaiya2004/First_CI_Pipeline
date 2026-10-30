import importlib

intersection_mod = importlib.import_module("28_set_intersection")
find_intersection = intersection_mod.find_intersection

def test_intersection_basic():
    assert find_intersection([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

def test_intersection_no_common():
    assert find_intersection([1, 2], [3, 4]) == []

def test_intersection_duplicates():
    assert find_intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3]

def test_intersection_empty():
    assert find_intersection([], [1, 2]) == []
