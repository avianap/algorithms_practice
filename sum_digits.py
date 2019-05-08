def sum_digits(n):
    """Sum all the digits in the number n
    O(log n)

    Args:
        n (int)

    Returns:
        int: sum of digits
    """
    s = 0
    for digit in str(n):
        s += int(digit)
    return s


def sum_digits_no_string(n):
    """Sum all the digits in the number n (not using strings)
    O(log n)

    Args:
        n (int)

    Returns:
        int: sum of digits
    """       
    s = 0
    while n > 0:
        r = n % 10
        s += r
        n = (n-r)/10
    return s




if __name__ == "__main__":
    print(sum_digits(222))
    print(sum_digits(444))
    print(sum_digits_no_string(222))
    print(sum_digits_no_string(444))

