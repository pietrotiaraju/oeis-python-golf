m=0
while 1:x=B=8<<m;k=m+1;exec("x=4*B**m+2*B+B*x//(B**k+1)**2;k-=1;"*k);print(x//4%B-B//2);m+=2
