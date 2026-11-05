A=[n:=1]*2
while p:=1:
 while p*p*n%576:p+=1
 print(A[n]*p//24);n+=1;p=2
 while n%p:p+=1
 A+=A[n//p]*(p+(n%p**2>0)),
