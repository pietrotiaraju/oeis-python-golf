def s(n):
 p=2;t=1
 while p*p<=n:
  a=1
  while n%p<1:n//=p;a=a*p+1
  t*=a;p+=1
 return t*(n+1)if n>1 else t
a=b=1
while[print(a)]:a,b=b,s(a)+s(b)
