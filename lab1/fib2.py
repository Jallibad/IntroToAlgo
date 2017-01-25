import time
import matplotlib.pyplot as plt

def fib2(n):
    if n==0:
        return 0
    f = [1]*(n+1)
    f[0] = 0
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

#ns = [2**10,2**12,2**13,2**16,2**18,2**19]
ns = [1,5,10,15,20,25,30,35,40,41,42,43]
results = []
for n in ns:
    start_time = time.time()
    fib2(n)
    results.append(time.time()-start_time)
    print(results[-1])

plt.plot(ns, results, label='fib2')
plt.xlabel('n')
plt.ylabel('time')
plt.title('fib2')
plt.legend()
plt.show()
