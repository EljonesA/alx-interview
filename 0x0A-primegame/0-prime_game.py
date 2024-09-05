#!/usr/bin/python3
""" Prime Game Algorithm """


def isWinner(x, nums):
    """
    Determines the winner of a prime number game played between Maria and Ben.

    In the game, given set of consecutive integers from 1 to n for each round,
    Maria and Ben take turns choosing a prime number from the set and removing
    that prime number and all of its multiples from the set. Maria always goes
    first. The player who cannot make a move loses the game.

    The function simulates `x` rounds of this game, where `n` can be different
    for each round, and determines who wins the most rounds, Maria or Ben.

    Parameters:
    -----------
    x : int
        The number of rounds to be played.
    nums : list of int
        An array where each element is the number `n` for each round (the set
        contains numbers from 1 to n).

    Returns:
    --------
    str or None
        Returns the name of the player who won the most rounds ("Maria"/ "Ben")
        If the number of wins is tied, returns None.

    Example:
    --------
    >>> isWinner(3, [4, 5, 1])
    'Ben'

    Explanation:
    1st round (n = 4): Maria picks 2 and removes 2 and 4. Ben picks 3 and
    removes 3. Ben wins.
    2nd round (n = 5): Maria picks 2 and removes 2 and 4. Ben picks 3 and
    removes 3. Maria picks 5 and wins.
    3rd round (n = 1): Ben wins since no prime numbers are available
    for Maria to pick.

    Constraints:
    ------------
    - 1 <= x <= 10000
    - 1 <= nums[i] <= 10000 for all i
    """
    if not nums or x < 1:
        return None

    # find maximum value of n in nums to limit sleve size
    max_n = max(nums)

    # 1: sieve of Eratosthenes to find all primes up to max_n
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
        # If the number of primes up to n is odd, Maria wins
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
