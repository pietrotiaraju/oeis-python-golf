from math import*
r=[];n=3;L=1
while 1:j=0;r=[x:=L]+[x:=(j:=j+2)**2*a*n-x for a in r];L*=n;print(x//gcd(x,L//(n-2)));n+=2
