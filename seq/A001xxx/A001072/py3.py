from itertools import*
c=lambda F,s={0}:[s:=s|{v for e in F if{*e}&s for v in e}for _ in R]and s>={*R}
n=3
while[R:=range(n),print(len({min(sum(1<<2**p[x]+2**p[y]for x,y in F)for p in permutations(R))for r in range(n*n)for F in map({(0,1),(0,2)}.union,combinations(combinations(R[1:],2),r))if all(c(F-{e})>all(c(F-{e,f})for f in F)for e in F)}))]:n+=1
