from fractions import*
n=0
while 1:
 P=[1]
 for k in range(1,n+1):P+=sum(Fraction((2-2*n)*j-3*k,2*j+3)*P[-j]for j in range(1,k+1))/k,
 print(P[n].denominator);n+=1
