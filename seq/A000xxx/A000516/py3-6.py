from itertools import*
n=1
while R:=range(n):print(len({min(sum(6**sum(1<<q[j]for j in r)for r in M)for q in permutations(R))for M in combinations_with_replacement(combinations(R,5),n)if max(map(sum(M,()).count,R))<6}));n+=1
