from itertools import*
n=2
while 1:R=range(n);print(len({min(sum(4**(2**p[a]+2**p[b])for a,b in E)for p in permutations(R))for E in combinations_with_replacement(combinations(R,2),n*3//2)if len(dict(E))>n-2and{*map(sum(E,()).count,R)}=={3}}));n+=2