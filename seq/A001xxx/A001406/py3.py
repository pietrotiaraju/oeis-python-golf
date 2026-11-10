import math
n=0
while 1:
 S=n+1;X=8**S**3;Y=X**(2*n);M=X*Y;P=1;Q=[[(1+X)**(k-j)*(1-X)**j+(1-X)**(k-j)*(1+X)**j for j in range(k+1)]for k in range(9)]
 for e in range(32):V=[(x,y,z)for x in range(S-e%2)for y in range(S-e//2%2)for z in range(S-e//4%2)if(x+e//8)%2==(y+e//16)%2==z%2];A,R=sorted([[v for v in V if v[2]%2^r]for r in(0,1)],key=len);N=[sum(1<<i for i,a in enumerate(A)if math.dist(a,b)<2)for b in R];P*=pow(sum(math.prod(Q[m.bit_count()][(g&m).bit_count()]for m in N)for g in range(1<<len(A)))>>len(V),(-1)**(e%8).bit_count(),M)
 print((P+Y*-~X//2)%M//Y-X//2);n+=1
