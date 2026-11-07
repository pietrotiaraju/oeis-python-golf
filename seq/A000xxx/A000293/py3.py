P=1,2,3,5,7;D={frozenset()}
while[print(len(D))]:D={S^{c}for S in D for s in S|{1}for p in P if{c//q for q in P if(c:=s*p)%q<1}<=S^{c}}