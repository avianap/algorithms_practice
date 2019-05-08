def product(a,b):
    """Computes a*b
    O(b)

    Args:
        a (int): positive integer
        b (int): positive integer

    Returns:
        int: product of a and b
    """
    s = 0
    for i in range(b):
        s += a
    return s

def power(a,b):
    """Computes a^b
    O(b)

    Args:
        a (int): positive integer
        b (int): positive integer

    Returns:
        int: a raised to the b
    """
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

def power_loop(a,b):
    """Computes a^b
    O(b)

    Args:
        a (int): positive integer
        b (int): positive integer

    Returns:
        int: a raised to the b
    """
    result = 1
    for i in range(b):
        result = result * a
    return result
    
def mod(a,b):
    """Computes a mod b
    O(1)

    Args:
        a (int): positive integer
        b (int): positive integer

    Returns:
        int: a mod b
    """
    floor = int(a/b)
    return a-b*floor

def div(a,b):
    """Computes a//b
    O(a/b)

    Args:
        a (int): positive integer
        b (int): positive integer

    Returns:
        int: a//b
    """
    s = b
    count = 0
    while s <= a:
        s += b
        count += 1
    return count


def sqrt_helper(n, start, end):
    """Finds the square root of a number n via binary search
    O(log n)

    Args:
        n (int): number to find square root of
        start (int): start of square root search range
        end (int): end of square root search range

    Returns:
        int: either square root of n OR -1 if number has no square root
    """
    if end < start:
        return -1 

    mid = (start+end)//2
    
    if mid*mid == n:
        return mid
    elif mid*mid > n:
        return sqrt_helper(n, start, mid-1)
    else: 
        return sqrt_helper(n, mid+1, end)

def sqrt(n):
    return sqrt_helper(n,1,n)

def naive_sqrt(n):
    """Finds the square root of a number n via incremental guessing
    O(sqrt(n))

    Args:
        n (int)

    Returns:
        int: either square root of n OR -1 if the number has no square root
    """
    for guess in range(n):
        if guess*guess == n:
            return guess
        elif guess*guess > n:
            return -1
        

if __name__ == "__main__":
    print(product(1,2))
    print(product(3,5))
    print(power(2,4))
    print(power(3,3))
    print(power_loop(3,3))
    print(power_loop(2,4))
    print(mod(10,3))
    print(mod(11,3))
    print(div(10,3))
    print(div(8,3))
    print(sqrt(16))
    print(sqrt(5))
    print(naive_sqrt(16))
    print(naive_sqrt(5))
