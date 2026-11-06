from itertools import*
n=2
while 1:
 R=range(n);S=set();c=0
 for E in combinations_with_replacement(combinations(R,2),n*3//2):
  if any(sum(E,()).count(i)!=3for i in R):continue
  V={0}
  for _ in R:V|={b for e in E if V&{*e}for b in e}
  if len(V)==n and E not in S:c+=1;S|={tuple(sorted(tuple(sorted((p[a],p[b])))for a,b in E))for p in permutations(R)}
 print(c);n+=2
