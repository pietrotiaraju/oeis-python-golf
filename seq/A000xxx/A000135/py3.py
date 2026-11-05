c=lambda v,t:v<t**3and c(v,(2*t+v//t//t)//3)or t
f=lambda b,i:b<W[i]or f(b-W[i],i+1)+f(b,i+1)
n=M=1
while 1:M*=2;a,b=[f(n*M,0)for e in(0,1)if[W:=[c(t*t*M-e,t)+e for t in range(M,3*n*n*M,M)]]];n+=a==b!=print(a-1)
