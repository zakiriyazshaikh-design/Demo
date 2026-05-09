def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def generate_primes(limit: int) -> list:
    return [num for num in range(2, limit + 1) if is_prime(num)]


if __name__ == "__main__":
    limit = 50
    primes = generate_primes(limit)

    print(primes)
