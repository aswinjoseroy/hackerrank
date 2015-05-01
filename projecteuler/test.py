def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.add(i)
    return i

def find_primes(n):
    primes = set([2])
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return primes
        i += 1
        

def primes(n):
        """ Returns  a list of primes < n """
        sieve = [True] * n
        for i in xrange(3,int(n**0.5)+1,2):
            if sieve[i]:
                sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
        return [2] + [i for i in xrange(3,n,2) if sieve[i]]
                
p = primes(100000)
print p

#98299