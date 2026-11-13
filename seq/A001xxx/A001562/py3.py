import math
k=P=1
while 1:P*=k*-~k;k+=2;N=10**k//11+1;P%k*all(N%d for d in range(2*k+1,math.isqrt(N)+1,2*k))and print(k)
