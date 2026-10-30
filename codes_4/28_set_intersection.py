"""Program 28: Find the intersection of two lists."""
def find_intersection(list1, list2):
    """Return a sorted list containing elements common to both lists."""
    return sorted(list(set(list1) & set(list2)))

if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5]
    l2 = [4, 5, 6, 7, 8]
    print("Intersection:", find_intersection(l1, l2))
