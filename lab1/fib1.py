import time
import matplotlib.pyplot as plt

def fib1(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib1(n-1) + fib1(n-2)

ns = [1,5,10,15,20,25,30,35,40,41,42,43]
results = []
for n in ns:
    start_time = time.time()
    fib1(n)
    results.append(time.time()-start_time)
    print(results[-1])

plt.plot(ns, results, label='fib1')
plt.xlabel('n')
plt.ylabel('time')
plt.title('fib1')
plt.legend()
plt.show()
