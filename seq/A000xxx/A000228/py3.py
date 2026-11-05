D=1,1j,1j-1,-1,-1j,1-1j;F=frozenset;S=[F({0})]
while[print(len(S))]:S={F(F(u*w.real+v*w.imag for w in[len(Q)*z-sum(Q)for z in Q])for u in D for v in D if u-v in D):Q for P in S for Q in{P|{z+d}for z in P for d in D}-{P}}.values()
