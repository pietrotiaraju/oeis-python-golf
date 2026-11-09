from itertools import*
n=1
while R:=range(n):c=lambda M:min(sum(5**sum(r[j]<<q[j]for j in R)for r in M)for q in permutations(R));print(len({x for M in combinations_with_replacement([[j in t for j in R]for t in combinations(R,4)],n)if max(map(sum,zip(*M)))<5and(x:=c(M))==c([*zip(*M)])}));n+=1
