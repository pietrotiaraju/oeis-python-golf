def f(n):
 p=2
 while p*p<=n:
  e=0
  while n%p<1:n//=p;e+=1
  while e:
   if e%3==2:return 0
   e//=3
  p+=1
 return 1
n=1
while 1:
 if f(n):print(n)
 n+=1
