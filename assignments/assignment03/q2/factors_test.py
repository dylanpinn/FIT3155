import factors


class TestFactors:
    def test_simple(self):
        expected = [(4, [(2, 2)]), (3, [(3, 1)])]
        assert factors.PrimeFactors(5).factors() == expected

    def test_length_of_factors(self):
        assert len(factors.PrimeFactors(1000).factors()) == 100

    def test_228(self):
        expected = [(2, 2), (3, 1), (19, 1)]
        assert factors.PrimeFactors(100).prime_factors(228) == expected

    def test_189(self):
        expected = [(3, 3), (7, 1)]
        assert factors.PrimeFactors(100).prime_factors(189) == expected

    def test_300(self):
        expected = [(2, 2), (3, 1), (5, 2)]
        assert factors.PrimeFactors(100).prime_factors(300) == expected

    def test_primes(self):
        f = factors.PrimeFactors(10)
        for i in range(1, 20000):
            assert f.naive_prime(i) == f.miller_rabin_prime_test(i)
