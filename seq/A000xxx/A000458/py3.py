def s(n):
 p=t=1
 while p*p<n:
  p+=1;a=1
  while n%p<1:n//=p;a=a*p+1
  t*=a
 return t*(n+(n>1))
a=b=1
while[print(a)]:a,b=b,s(a)+s(b)
