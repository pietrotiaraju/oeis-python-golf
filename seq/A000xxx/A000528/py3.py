from itertools import*
n=0
while Q:=[*permutations(range(n:=n+1))]:print(len({f"{min(sorted([z.index(b[a.index(s)])for s in z]for b in T)for T in(L,[*zip(*L)])for z in Q for a in T)}"for L in product(*[[p for p in Q if p[k]*n+k==p[0]]for k in Q[0]])if{*zip(*L)}<={*Q}}))
