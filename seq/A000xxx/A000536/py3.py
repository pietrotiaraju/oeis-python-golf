from functools import*
@cache
def f(n,j):return n*f(n-1,0)+(-1)**n if j==0 and n else (n*(n+1-2*j)*f(n-1,j-1)+n*(n-1)*f(n-2,j-1))//j if n>=2*j>0 else int(n==j==0)
n=4
while 1:print(f(n,2));n+=1
