P=range(1,14);D={frozenset({1})}
while[print(len(D))]:D={S^{c}for S in D for s in S for p in P if{c//q for q in P if(c:=s*p)%q<1}<=S^{c}}