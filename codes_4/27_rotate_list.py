"""Program 27: Rotate a list by k positions."""
def rotate_list(arr, k):
    """Rotate the list to the right by k positions."""
    if not arr:
        return []
    k = k % len(arr)
    if k == 0:
        return list(arr)
    return arr[-k:] + arr[:-k]

if __name__ == "__main__":
    user_input = [1, 2, 3, 4, 5]
    k = 2
    print("Rotated list:", rotate_list(user_input, k))
