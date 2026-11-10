from math import*
C=comb;m=2
while 1:R=range(m);print((m>2)*sum((-1)**(a+b)*C(2*m-1-a-b,m+~a)*C(m-b,2)*C(2*m-2,a)*C(2*m,b)*((k:=m*m-m)-a*b)for a in R for b in R)//k);m+=1
