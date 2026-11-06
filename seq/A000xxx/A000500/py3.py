from math import*
n=7
while 1:
 B=(4*n)**n;z=B*B;w=z*z;a=b=c=0;d=1
 for v in([0,-2*z,-2*z*(1+B),3*w]+[0]*n)[:n]:a,b,c,d=b,c,d,(1+3*B)*d-2*z*c-z*(1+B)*b+w*a+v
 print(sum((-1)**(k-7)*comb(k,7)*perm(n-k)*(d//B**k%B)for k in range(7,n+1)));n+=1
