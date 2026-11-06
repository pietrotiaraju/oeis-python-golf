from math import*
n=a=m=0
while 1:
 n+=1;S=6*n**47;x=p=2*S;i=1;A=1+4*sum(isqrt(n-i*i)for i in range(isqrt(n)+1))
 while x:=x*i//(i-~i):p+=x;i+=1
 if abs(F:=A*S-p*n)>abs(a*S-p*m):a=A;m=n;print((F+S//2)//S)
