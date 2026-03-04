"""
Find the sum of all prime numbers under 100,000
"""
from math import sqrt

LIMIT = 100_000

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

assert is_prime(1) is False
assert is_prime(2) is True
assert is_prime(3) is True
assert is_prime(4) is False
assert is_prime(5) is True
assert is_prime(6) is False

sum_ = 0

for num in range(1, LIMIT):
    if is_prime(num):
        sum_ += num

assert sum_ == 454_396_537
print(f"{sum_:,}")