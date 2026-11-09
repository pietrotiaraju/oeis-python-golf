from itertools import*
n=1
while R:=range(n):print(len({min(sum(5**sum(1<<q[j]for j in r)for r in M)for q in permutations(R))for M in combinations_with_replacement(combinations(R,4),n)if max(map(sum(M,()).count,R))<5}));n+=1
