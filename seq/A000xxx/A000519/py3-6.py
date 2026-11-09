from itertools import*
n=1
while R:=range(n):print(len({min(sum(1<<n*sum(1<<q[j]for j in r)for r in M)for q in permutations(R))for k in R for M in combinations_with_replacement(combinations(R,k+1),n)if max(map(sum(M,()).count,R))<k+2}));n+=1
