import math
f=lambda r,*L:r<1or sum(f(r+k,*L,k)<<-k//2+sum(map(math.gcd,L,[k]*n))for k in range(-r,0))//r
R=1,;C=[0];n=s=0
while[print(s)]:R=f(n:=n+1),*R;s=sum(d*C[d]*sum(R[d::d])for d in range(1,n))//n;C+=R[0]-s,
