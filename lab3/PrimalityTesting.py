import random

def modexp(x,y,n):
    if y==0:
        return 1
    z = modexp(x, y//2, n)
    if y%2 == 0:
        return z*z % n
    else:
        return x*z*z % n

def primality(n, k=100):
    for _ in range(k):
        if modexp(random.randint(1,n-1), n-1, n) != 1:
            return False
    return True

def primality2(n, k=1000):
    primes = 0
    for _ in range(k):
        if modexp(random.randint(1,n-1), n-1, n) == 1:
            primes += 1
    return 100 * (1-(primes/k))

def main():
    # checkpoint 1
    for i in range(2,20):
        print("{0} is {1}prime".format(i, "" if primality(i) else "not "))

    print("\n**********\n")
    # checkpoint 2
    carmichaels = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881]
    for i in carmichaels:
        print("{0} has {1:.0f}% of tests pass".format(i, primality2(i)))

if __name__ == "__main__":
    main()
