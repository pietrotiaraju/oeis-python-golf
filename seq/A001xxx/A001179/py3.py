n=0
while 1:
 k=n=n+1;m=c=0
 while k-m:
  m=k;a=b=k=1
  while a%m|~-b%m:a,b=b,a+b;k+=1
 while k>4:k//=5;c+=1
 print(c)
