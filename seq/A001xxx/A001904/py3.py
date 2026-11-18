from math import*
r=[];n=L=1
while 1:j=-1;r=[x:=L]+[x:=(j:=j+2)**2*a*n-x for a in r];L*=n;print(x//gcd(x,L));n+=2
