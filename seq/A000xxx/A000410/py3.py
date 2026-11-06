from itertools import*
s=lambda A:bool(A)and(not(p:=next((r for r in A if r[0]),[]))or s([[p[0]*x-r[0]*y for x,y in zip(r[1:],p[1:])]for r in A if r is not p]))
n=1
while 1:
 R=range(n);print(sum(s([[x>>i&1 for i in R]for x in V])for V in combinations(range(1,1<<n),n)));n+=1
