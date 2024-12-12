#!/usr/bin/python3
def isWinner(x, nums):
    """Determine the winner of the Prime Game."""
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        if play_game(n, primes):
            wins["Maria"] += 1
        else:
            wins["Ben"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(max_n):
    """Compute a list of prime indicators up to max_n using Sieve of Eratosthenes."""
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    return primes


def play_game(n, primes):
    """Simulate the game for a given n and return True if Maria wins, False otherwise."""
    remaining_numbers = set(range(1, n + 1))
    maria_turn = True

    while True:
        # Find the next available prime
        next_prime = next(
            (num for num in remaining_numbers if primes[num]), None)
        if next_prime is None:
            return not maria_turn  # The player who cannot move loses

        # Remove the prime and its multiples
        to_remove = set(range(next_prime, n + 1, next_prime))
        remaining_numbers -= to_remove

        # Switch turn
        maria_turn = not maria_turn
