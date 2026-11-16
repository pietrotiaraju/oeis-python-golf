from fractions import*
from math import*
B=[[0,1]]
while[print(lcm(*[c.denominator for c in B[-1]]))]:m=len(B);B+=[m]+[sum(comb(m+1,i)*(i*sum(P[j:j+1])+(m-i)*sum(P[j-1:j]))for i,*P in B)/Fraction(m*~m)for j in range(m+1)],