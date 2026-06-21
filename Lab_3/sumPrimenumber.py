# Method 1: Simple prime checking

def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    if n < 2:
        return False
    # Check divisibility from 2 up to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Find the sum of all primes below 1000
total = 0

for num in range(2, 1000):
    if is_prime(num):
        total += num

print(f"The sum of all prime numbers below 1000 is: {total}")