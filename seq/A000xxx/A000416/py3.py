R=range(2,18)
S={frozenset({1})}
while[print(len(S))]:S={s|{p}for s in S for p in{q*r for q in s for r in R}-s if{p//r for r in R if p%r<1}<=s}
