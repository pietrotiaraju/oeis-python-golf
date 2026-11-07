f=lambda n:n>1and-~f([n//2,3*n+1][n%2])
D={};k=n=r=1;t=0
while s:=f(n:=n+1):D={r*(s!=t):t}|D;r=r*(s==t)+1;t=s;k+=k in D!=print(D[k])
