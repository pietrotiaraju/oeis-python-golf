from itertools import*
for n in count():R=range(2*n);print(len({min(sum(1<<2**p[a]+2**p[b]for a,b in G)for p in permutations(R))for G in combinations(combinations(R,2),n)}))
