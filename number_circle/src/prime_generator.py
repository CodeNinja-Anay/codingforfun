"""
prime generator module. Provides mechanism to generate prime number.
Contains functions for returning list of prime numbers.
"""


def prime_generator(user_value):
    """
    Generates a list of prime numbers between min_number and max_number inclusive.

    Args:
        min_number (int): Lower bound of range (inclusive)
        max_number (int): Upper bound of range (inclusive)

    Returns:
        list: List of prime numbers in the specified range
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [num for num in range(1, user_value) if is_prime(num)]
