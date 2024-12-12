#!/usr/bin/python3
"""
Solution to the Prime Game problem.

This module implements the isWinner function which determines the winner
of a game where players take turns removing prime numbers and their multiples
from a set of consecutive integers.
"""

def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check for primality
    
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def remove_multiples(nums, prime):
    """
    Remove a prime number and its multiples from the set.
    
    Args:
        nums (list): Current set of numbers
        prime (int): Prime number to remove
    
    Returns:
        list: Updated set of numbers
    """
    return [num for num in nums if num % prime != 0]

def play_game(n):
    """
    Simulate a single round of the prime game.
    
    Args:
        n (int): Maximum number in the set
    
    Returns:
        str: Winner of the game ('Maria' or 'Ben')
    """
    # Initialize the game
    nums = list(range(1, n + 1))
    current_player = 'Maria'
    
    while True:
        # Find the list of primes in the current set
        primes = [num for num in nums if is_prime(num)]
        
        # If no primes remain, current player loses
        if not primes:
            return 'Ben' if current_player == 'Maria' else 'Maria'
        
        # Remove the smallest prime and its multiples
        prime_to_remove = min(primes)
        nums = remove_multiples(nums, prime_to_remove)
        
        # Switch players
        current_player = 'Ben' if current_player == 'Maria' else 'Maria'

def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of the prime game.
    
    Args:
        x (int): Number of rounds
        nums (list): Maximum numbers for each round
    
    Returns:
        str: Name of the player who won the most rounds
    """
    if not nums or x <= 0:
        return None
    
    # Play each round and track wins
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Determine overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
