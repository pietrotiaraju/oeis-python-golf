U=1,1j,-1,-1j;F=frozenset;S=[F([0])]
K=lambda Q,f=2,c=0:F(F(u*((w:=len(Q)*z-sum(Q))-m*w.real)+(z*z+c).real%2*f/4for z in Q)for m in(0,f)for u in U)
while[print(sum((K(Q)!=K(Q,2,1))+1for Q in S))]:S={K(Q,0):Q for P in S for Q in{P|{z+d}for z in P for d in U}-{P}}.values()
