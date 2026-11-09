m=0;k=1
while 1:L=sorted(a**3+b**3+c**3for c in range(k)for b in range(c+1)for a in range(b+1));[print(m:=x)for x,y in zip(L,L[1:])if m<x==y<k**3];k*=2
