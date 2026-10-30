"""Program 29: Check if a number is an Armstrong number."""
def is_armstrong(num):
    """Return True if num is an Armstrong number, False otherwise."""
    if num < 0:
        return False
    str_num = str(num)
    power = len(str_num)
    total = sum(int(digit) ** power for digit in str_num)
    return total == num

if __name__ == "__main__":
    user_input = int(input("Enter a number: "))
    print("Is Armstrong:", is_armstrong(user_input))
