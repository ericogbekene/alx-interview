#!/usr/bin/python3
"""
Maria and Ben Playing a game of Prime Numbers.
Who Wins
"""

def isWinner(x, nums):
    """
    checks the winner of x rounds
    of Prime Game
    
    Args: x, nums
    Returns: True if Maria wins, False if Ben wins
    """
    
    def sieve_prime(n):
        """
        helper function to get prime number
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n+1, i):
                    primes[j] = False
        return primes
    
    def play_game(n):
        primes = sieve_prime(n)
        player = "Maria"
        while True:
            for i in range(2, n + 1):
                if primes[i]:
                    primes[i] = False
                    for j in range(i * 2, n + 1, i):
                        primes[j] = False
                    break
            else:
                return player
            player = "Ben" if player == "Maria" else "Maria"
    '''
    
    def play_game(n):
        prime_num = sieve_prime(n)
        turn = 0  # 0 for Maria, 1 for Ben
        for i in range(2, n + 1):
            if prime_num[i]:
                turn += 1
                for j in range(i, n + 1, i):
                    prime_num[j] = False
        return "Maria" if turn % 2 == 1 else "Ben"
    '''

    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
