from itertools import*
from math import*
def h(F,P,k):
 c=len(P)
 return k<1 or(h(F+P,[],k-1)if c==n else any(h(F,P+[s],k)for s in permutations(range(n))if s[0]==c and(F or s[c]<1)and all(sum(map(int.__eq__,s,q))==(q in F)for q in F+P)))
n=l=1
while n:=n+1:
 k=1;q=l<(l:=lcm(l,n))
 while k<n-1and(q or h([],[],k+1)):k+=1
 print(k)
