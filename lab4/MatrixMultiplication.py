import numpy
import time

def basic(x,y):
    n = x.shape[0]
    ans = numpy.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i,j] += x[i,k]*y[k,j]
    return ans

def strassen(x,y):
    n = x.shape[0]
    if n == 1:
        return numpy.array([[x[0,0]*y[0,0]]])
    xs = [numpy.hsplit(f, 2) for f in numpy.vsplit(x, 2)]
    a = xs[0][0]
    b = xs[0][1]
    c = xs[1][0]
    d = xs[1][1]
    ys = [numpy.hsplit(f, 2) for f in numpy.vsplit(y, 2)]
    e = ys[0][0]
    f = ys[0][1]
    g = ys[1][0]
    h = ys[1][1]
    p1 = strassen(a,f-h)
    p2 = strassen(a+b,h)
    p3 = strassen(c+d,e)
    p4 = strassen(d,g-e)
    p5 = strassen(a+d,e+h)
    p6 = strassen(b-d,g+h)
    p7 = strassen(a-c,e+f)
    return numpy.vstack((numpy.hstack((p5+p4-p2+p6,p1+p2)),numpy.hstack((p3+p4,p1+p5-p3-p7))))

###n = int(input("n: "))
##for n in [16,32,64,128,256,512,1024]:
##    x = numpy.random.random((n,n))
##    y = numpy.random.random((n,n))
##    print(n)
##    start_time = time.time()
##    basic(x,y)
##    print(time.time()-start_time)
##    start_time = time.time()
##    strassen(x,y)
##    print(time.time()-start_time)
##

x = numpy.random.random((4,4))
y = numpy.random.random((4,4))
