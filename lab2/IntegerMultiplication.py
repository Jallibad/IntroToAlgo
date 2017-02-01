import math
import time
import random

def method1(x, y):
    answer = 0
    i = 0
    while y != 0:
        if y & 1 != 0:
            answer += x << i
        y = y >> 1
        i += 1
    return answer

def method2(x, y):
    if y==0:
        return 0
    z = method2(x, y >> 1) << 1
    if y & 1 == 0: # if y is even
        return z
    else:
        return x+z

def method3(x, y):
    if x == 0 or y == 0:
        return 0
    n = max(x.bit_length(), y.bit_length())
    if n==1:
        return 1
    half = n >> 1
    xl = x >> half
    yl = y >> half
    xr = x & ((1 << half)-1)
    yr = y & ((1 << half)-1)
    p1 = method3(xl,yl)
    p2 = method3(xr,yr)
    p3 = method3(xl+xr,yl+yr)
    return (p1 << (~(~n | 1)))+((p3-p1-p2) << (n >> 1))+p2

d = int(input("Number of digits: "))
r = 10
method1Times = []
method2Times = []
method3Times = []
for _ in range(r):
    x = 0
    y = 0
    for _ in range(d):
        x = x*10 + random.randint(0,9)
        y = y*10 + random.randint(0,9)
    start_time = time.time()
    method1(x,y)
    method1Times.append(time.time()-start_time)
    start_time = time.time()
    method2(x,y)
    method2Times.append(time.time()-start_time)
    start_time = time.time()
    method3(x,y)
    method3Times.append(time.time()-start_time)
print("method1: ", sum(method1Times)/r)
print("method2: ", sum(method2Times)/r)
print("method3: ", sum(method3Times)/r)
