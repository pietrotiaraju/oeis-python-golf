import math
n=0
while n:=n+1:
 m=5*n;N=2*m;B=2*N;M=(B**N-1)//math.lcm(*[B**d-1for d in range(1,N)if N%d<1]);Z=[(B**e+B**(N-e))%M for e in range(m)];f=1+Z[2*n];S=0
 for r in 1,2:E=range(r,m,2);D={Z[e]:e for e in E};S+=sum(all(abs(u-v)<=2*n<=u+v<=8*n for u,v in zip((a,b,c,d,g),(b,c,d,g,a)))for a in E for b in E for c in E if(d:=D.get(x:=(f*(Z[c]-Z[b])+Z[a])%M))and(g:=D.get((f*(x-Z[c])+Z[b])%M))and((f-1)*Z[b]-Z[a]-Z[c])%M)
 print(n*S//2)
