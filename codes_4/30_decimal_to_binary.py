"""Program 30: Convert a decimal number to binary."""
def decimal_to_binary(n):
    """Return the binary representation of a non-negative integer as a string."""
    if n == 0:
        return "0"
    if n < 0:
        raise ValueError("Negative numbers are not supported for basic binary conversion.")
    
    binary_digits = []
    while n > 0:
        binary_digits.append(str(n % 2))
        n //= 2
    return "".join(reversed(binary_digits))

if __name__ == "__main__":
    user_input = int(input("Enter a decimal number: "))
    print("Binary representation:", decimal_to_binary(user_input))
