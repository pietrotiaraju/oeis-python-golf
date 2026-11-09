from fractions import*
h=[Fraction(1)];d=1
while 1:
 k=len(h)
 if k%2:print((h[-1]*d).denominator);d*=k
 h+=[(h[-1]/k-sum(h[-j]*h[j]/(j+1)for j in range(1,k)))*(k+1)/(k+2)]
