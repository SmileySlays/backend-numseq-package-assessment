def primes(n):
    """Returns list of primes up to n"""
    primes = []
    for i in range(n+1):
        if is_prime(i):
            primes.append(i)
    return primes


def is_prime(n):
    """Boolean if n is prime"""
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import sys
    print(prime(int(sys.argv[1])))