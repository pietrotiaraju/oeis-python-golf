from itertools import*
L=[frozenset()];R=[];b=1
while[print(len(L))]:
 W={X|{u|b for u in R}for X in L};R+=b,;Q=[*zip(*permutations(R))]
 for l in range(b):T={l}|{u|b for u in R if l&u};W|={w-T|{l|b}for w in W if T<=w}
 L=[e for e in[*W]if e in W!={*map(W.discard,map(set,zip(*[map(sum,zip(*[q for q in Q if m&q[0]]))for m in e])))}];b*=2
