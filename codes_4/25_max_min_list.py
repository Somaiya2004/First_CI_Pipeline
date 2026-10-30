"""Program 25: Find the maximum and minimum values in a list."""
def find_max_min(arr):
    """Return a tuple of (maximum, minimum) from the list.
    Returns (None, None) if the list is empty.
    """
    if not arr:
        return (None, None)
    
    maximum = arr[0]
    minimum = arr[0]
    for num in arr[1:]:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return (maximum, minimum)

if __name__ == "__main__":
    user_input = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Max and Min:", find_max_min(user_input))
