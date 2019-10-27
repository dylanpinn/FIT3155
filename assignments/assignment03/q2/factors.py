#!/usr/bin/env python3

"""
FIT3155 - Assignment 3

Semester 2 2019

Dylan Pinn 24160547


Q2: Factors
"""

import random
from collections import Counter
from typing import List, Tuple

Factors = Tuple[int, int]


class PrimeFactors:
    def __init__(self, n: int):
        self.n = n

    def factors(self) -> List[Tuple[int, List[Factors]]]:
        """Find prime factors for the 100 largest prime numbers less than n"""
        result = []
        for i in range(self.n - 1, 1, -1):
            # If i is prime then find prime factors for i+1
            if self.naive_prime(i):
                factors = self.prime_factors(i + 1)
                result.append((i, factors))
        return result

    @staticmethod
    def naive_prime(n: int) -> bool:
        """Naive check if number is prime."""
        if n <= 1:
            return False
        for k in range(2, n - 1):
            if n % k == 0:
                return False
        return True

    @staticmethod
    def miller_rabin_prime_test(n: int, k: int = 64) -> bool:
        """Miller-Rabin's Randomized Primality testing algorithm."""
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        # If n is even then composite.
        if n % 2 == 0:
            return False
        # Factor n- 1 as 2^s.t, where t is odd
        s = 0
        t = n - 1
        while t % 2 == 0:
            s += 1
            t //= 2

        def trial_composite(a: int) -> bool:
            """Check if number is composite or probably prime."""
            if pow(a, n - 1, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2 ** i * t, n) == n - 1:
                    return False
            return True

        # n-1 == 2^s.t, where t is odd
        # k random tests
        for _ in range(k):
            a = random.randrange(2, n - 1)
            if trial_composite(a):
                return False
        return True

    @staticmethod
    def prime_factors(n: int) -> List[Factors]:
        """Find prime factors of n."""
        factors = []
        p = 2
        while n >= p * p:
            if n % p == 0:
                factors.append(p)
                n = n // p
            else:
                p = p + 1

        factors.append(n)

        # Group factors in Tuples containing the factor and the exponent
        # e.g. [2, 2] == (2, 2)
        result = list(Counter(factors).items())
        return result
