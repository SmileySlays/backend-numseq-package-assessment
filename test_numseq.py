import sys
import timeit
sys.path.append('/Users/jakiepoo/Documents/KAQ3/backend-numseq-package-assessment')
from numseq.fib import fib
from numseq.geo import *
from numseq.prime import *


if __name__ == "__main__":
    """ Testing for numseq module functions"""
    test_fib = """
print("Fibonacci")
for i in range(10):
    print("{}: {}".format(i, fib(i)))
    """

    test_geo = """
print("Geometric numbers (square, triangle, cube)")
for i in range(10):
    print("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))
    """

    test_primes = """
print("Primes")
prime_list = primes(1000)
for p in prime_list[-10:]:
    print(p)
print("Is 999981 prime? {}".format(is_prime(999981)))
print("Is 999983 prime? {}".format(is_prime(999983)))
    """

    fib_time = timeit.timeit(test_fib, number=1, setup="from numseq.fib import fib")
    geo_time = timeit.timeit(test_geo, number=1, setup="from numseq.geo import square, triangle, cube")
    primes_time = timeit.timeit(test_primes, number=1, setup="from numseq.prime import primes, is_prime")
    print(fib_time)
    print(geo_time)
    print(primes_time)