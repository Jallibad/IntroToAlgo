import time
import matplotlib.pyplot as plt

def fib1(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib1(n-1) + fib1(n-2)

def fib2(n):
    if n==0:
        return 0
    f = [1]*(n+1)
    f[0] = 0
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

ns = [1,5,10,15,20,25,30,35,40,41,42,43]
fib1results = []
for n in ns:
    start_time = time.time()
    fib1(n)
    fib1results.append(time.time()-start_time)
    print(fib1results[-1])

fib2results = []
for n in ns:
    start_time = time.time()
    fib2(n)
    fib2results.append(time.time()-start_time)
    print(fib2results[-1])

plt.plot(ns, fib1results, label='fib1')
plt.plot(ns, fib2results, label='fib2')
plt.xlabel('n')
plt.ylabel('time')
plt.title('fib1 vs fib2')
plt.legend()
plt.show()
