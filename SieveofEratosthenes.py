def sieve_of_eratosthenes(n):
    # Step 1: Create a boolean array "prime[0..n]" and initialize all entries as True
    prime = [True for _ in range(n+1)]
    prime[0] = prime[1] = False  # 0 and 1 are not prime numbers

    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Mark all multiples of p as False
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Collect and return all prime numbers
    primes = [i for i in range(n+1) if prime[i]]
    return primes

# Example: Get all primes up to 50
print(sieve_of_eratosthenes(50))
