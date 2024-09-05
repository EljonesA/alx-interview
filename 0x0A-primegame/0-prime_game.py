#!/usr/bin/python3
""" Prime Game Algorithm """

def isWinner(x, nums):
    if not nums or x < 1:
        return None

    # find maximum value of n in nums to limit sleve size
    max_n = max(nums)

    #1: sieve of Eratosthenes to find all primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    # Prime count up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    # Step 2: Determine the winner for each game
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # If the number of primes up to n is odd, Maria wins (since she starts first)
        # If the number of primes up to n is even, Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 3: Return the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
