def f(n):
 t=0
 while n>1:t+=1;n=3*n+1 if n%2 else n//2
 return t
D={};n=k=r=1;t=0
while 1:
 n+=1;s=f(n)
 if s==t:r+=1
 else:D.setdefault(r,(n-r,t));r=1;t=s
 while k in D:print(D[k][0]);k+=1
