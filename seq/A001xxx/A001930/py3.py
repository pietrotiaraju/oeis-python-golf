from itertools import*
n=0;P=permutations
while 1:R=range(n);print(len({min(sum(1<<p[a]*n+p[b]for a,b in Q)for p in P(R))for k in range(1<<n)for Q in combinations(P(R,2),k)if{(a,c)for a,b in Q for x,c in Q if b==x!=c!=a}<={*Q}}));n+=1
