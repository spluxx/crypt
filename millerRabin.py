import random

# Make list of low primes
sieve = [1] * 200
for i in range(2,int((len(sieve))**0.5)+1):
    if sieve[i] == 0:
        continue
    for j in range(2*i,len(sieve),i):
        sieve[j] = 0
low_primes = [ i for i in range(2,len(sieve)) if sieve[i] ]

def isprime(n, num_trials=5):

    assert n > 0

    if n==1:
        return False

    # Low prime tests
    for p in low_primes:
        if n==p:
            return True
        if n%p == 0:
            return False


    # rewrite n-1 as 2**k * q
    # repeatedly try to divide n-1 by 2
    k = 0
    q = n-1
    while True:
        qnew, rem = divmod(q, 2)
        if rem == 1:
            break
        k += 1
        q = qnew

    def witness_composite(a):
        a = pow(a, q, n)
        if a == 1:
            return False
        for i in range(k):
            if a == n-1:
                return False
            a = pow(a,2,n)
        return True # n is definitely composite
 
    for i in range(num_trials):
        a = random.randrange(2, n)
        #print "Trying witness",a
        if witness_composite(a):
            return False
        
    return True
  
def nextprime(n):
    """Return smallest prime greater than or equal to n"""
    n |= 1 # Make odd
    while not isprime(n):
        n += 2
    
    return(n)

def nextsprime(n):
    """
    Return smallest prime ~greater than or equal to n, with (p-1)/2 also prime.
    """
    # A safe prime is always 11 mod 12
    n += 11 - n%12
    while not(isprime(n) and isprime((n-1)//2)):
        n += 12
    return n


    
    
