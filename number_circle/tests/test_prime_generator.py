from src.prime_generator import prime_generator

def test_prime_generator():
    primes = prime_generator(10)
    assert primes == [2, 3, 5, 7]