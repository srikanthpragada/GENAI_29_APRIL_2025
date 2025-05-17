def isPrime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isEven(num):
    """Check if a number is even."""
    return num % 2 == 0

def isPerfect(num):
    """Check if a number is perfect."""
    if num < 1:
        return False
    return sum(i for i in range(1, num//2 + 1) if num % i == 0) == num

def reverseNumber(num):
    """Reverse a number."""
    rev = 0
    n = abs(num)
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev if num >= 0 else -rev

