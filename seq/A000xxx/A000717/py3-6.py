from itertools import*
n=1
while R:=range(n):print(len({min(sum(1<<2**p[a]+2**p[b]for a,b in G)for p in permutations(R))for G in combinations(combinations(R,2),n*n-n>>2)}));n+=1
