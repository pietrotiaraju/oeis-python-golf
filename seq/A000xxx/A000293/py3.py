R=2,3,5,7
S={frozenset()}
while[print(len(S))]:S={s|{p}for s in S for p in{1,*{q*r for q in s for r in R}}-s if all(p%r or p//r in s for r in R)}
