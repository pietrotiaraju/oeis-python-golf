from math import*
C=comb;n=1
while 1:R=range(n);print((n>1)*sum((-1)**(a+b)*C(2*n-a-b,n+~a)*C(n-b+1,2)*C(2*n,a)*C(2*n,b)*(n*n-a*b)for a in R for b in R)//-n//n);n+=1
