def prime_generator(limit):
    """Генератор простих чисел."""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, limit):
        if is_prime(num):
            yield num
