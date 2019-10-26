import factors


class TestFactors:
    def test_simple(self):
        expected = [(3, [(2, 2)]), (2, [(3, 1)])]
        assert factors.PrimeFactors(5).factors() == expected

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
        for i in range(100, 1000):
            print(i)
            assert f.naive_prime(i) == f.miller_rabin_prime_test(i)

        assert f.miller_rabin_prime_test(547) is True
        assert f.miller_rabin_prime_test(548) is False
        assert f.naive_prime(541) is True
        assert f.miller_rabin_prime_test(541) is True
        assert factors.PrimeFactors(100).miller_rabin_prime_test(523) is True
        assert factors.PrimeFactors(100).miller_rabin_prime_test(521) is True
