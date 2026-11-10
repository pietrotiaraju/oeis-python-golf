from math import*
C=comb;f=factorial;n=0
while 1:R=range(n+1);print(sum(C(n,k)**2*C(k,j)*f(k)*f(3*n-3*k+j)*12**k*(-3)**j>>j for k in R for j in R)//36**n);n+=1
