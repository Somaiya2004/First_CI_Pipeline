"""Program 26: Find the sum of all numbers in a list."""
def sum_of_list(arr):
    """Return the sum of elements in the list. Returns 0 for an empty list."""
    total = 0
    for num in arr:
        total += num
    return total

if __name__ == "__main__":
    user_input = [1, 2, 3, 4, 5]
    print("Sum of list:", sum_of_list(user_input))
