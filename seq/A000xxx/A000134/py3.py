p=k=1
while u:=p:
 k+=2;j=b=0
 while b*b<u*u:b=b*j*j+u;j+=4;u*=-k*k
 if b<0:print(k//2);p=-p
