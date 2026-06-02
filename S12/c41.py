def binary_to_decimal(binary_str):
    """
    Function to convert a binary string to its decimal integer representation.
    
    Parameters:
    binary_str (str): The binary string to convert.
    
    Returns:
    int: The decimal representation of the binary string.
    """
    # Your code here
    decimal = 0
    power = 0

    for i in range(len(binary_str) - 1, -1, -1):
        decimal = decimal + int(binary_str[i]) * (2 ** power)
        power += 1

    return decimal

binary_str = input("Enter a binary number: ")
res = binary_to_decimal(binary_str)
print(res)

