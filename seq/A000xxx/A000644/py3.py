from itertools import*
d=n=4
while[print(len({min(t[j:]+t[:j]for t in(t,t[::-1])for j in range(n))for t in product(*[(1,-1)]*n)if sum(t)+(p:=0)==4if len({p+(p:=p+(d:=d*1j*x))for x in t})-n==p*n}))]:n+=4
