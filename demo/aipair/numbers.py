def isprime(n : int) -> bool:
    """Returns True if n is a prime number, False otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def isperfect(n : int) -> bool:
    """Returns True if n is a perfect number, False otherwise."""
    if n <= 0:
        return False
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_of_divisors == n

