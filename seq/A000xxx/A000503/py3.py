n=0
while 1:
 a,b,c,d,k=n,0,1,1,3
 while-b%(d or 1)*(2*c-k*d)<n**k:a,b,c,d=k*a-n*n*b,a,k*c-n*n*d,c;k+=2
 print(b//d);n+=1
