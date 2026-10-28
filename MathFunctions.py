from decimal import Decimal, getcontext

def calculate_pi(places):
    """

    :type places: int
    """
    getcontext().prec = places + 3

    # Chudnovsky Algorithm for high-precision Pi
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, (places // 14) + 2):
        M = (M * (K ** 3 - 16 * K)) // (i ** 3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / Decimal(X)
        K += 12

    pi = C / S

    return str(pi)[:places + 2]


def calculate_fibonacci(terms):
    """
    Return the first `terms` Fibonacci numbers joined into one string of digits,
    e.g. 8 terms -> "011235813".

    :type terms: int
    """
    a, b = 0, 1
    digits = ""
    for _ in range(terms):
        digits += str(a)
        a, b = b, a + b

    return digits


def calculate_primes(count):
    """
    Return the first `count` primes joined into one string of digits,
    e.g. 6 primes -> "23571113".

    :type count: int
    """
    primes = []
    candidate = 2
    while len(primes) < count:
        if all(candidate % p for p in primes if p * p <= candidate):
            primes.append(candidate)
        candidate += 1

    return "".join(str(p) for p in primes)


def calculate_golden_ratio(places):
    """
    The golden ratio, (1 + sqrt(5)) / 2, to `places` decimal places.

    :type places: int
    """
    getcontext().prec = places + 3
    phi = (1 + Decimal(5).sqrt()) / 2

    return str(phi)[:places + 2]


def calculate_collatz(start):
    """
    The Collatz sequence from `start` down to 1 (halve if even, 3n + 1 if odd).
    Each value becomes one digit, its last digit, so every step plays one chord.

    :type start: int
    """
    n = start
    digits = str(n % 10)
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        digits += str(n % 10)

    return digits