f=lambda n:n>1and-~f(n%2*(5*n+2)+n>>1)
D={};n=p=k=1
while n:=n+1:f(n)==f(n-1)or[D:={n-p:p}|D,p:=n];k+=k in D!=print(D[k])
