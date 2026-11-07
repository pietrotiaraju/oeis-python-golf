from math import*
n=1
while n:=n+1:
 m=0;S=[[a,0]for a in range(n)if gcd(a,n)<2]
 while S:
  x=len(F:=S.pop());a=F[0];d=gcd(a-1,n);p=2;m+=x-1>m
  while x%p:p+=1
  S+=[F+[c]for c in[(F[p%x]+F[x//p])%d][:p<x]or range(d)if c*2<=d*~-x>0<c|F[-1]if n%(x*(2+(x&2)))or~c+sum(i*2<a<i*x%a*2for i in range(a))&1]
 print(m)
