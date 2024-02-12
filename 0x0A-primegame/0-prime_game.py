#!/usr/bin/python3
""" Module for Prime Game
"""
def isWinner(x, nums):
    """
    function for calculating prime numbers
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_next_prime(current):
        next_prime = current + 1
        while not is_prime(next_prime):
            next_prime += 1
        return next_prime

    def game_winner(n):
        primes = [2]
        current = 2
        while current <= n:
            current = get_next_prime(current)
            primes.append(current)
            for multiple in range(current * 2, n + 1, current):
                if multiple in primes:
                    primes.remove(multiple)
        return "Maria" if len(primes) % 2 == 0 else "Ben"

    winners = [game_winner(n) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
