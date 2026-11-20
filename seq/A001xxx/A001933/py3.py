U=1,1j,-1,-1j;F=frozenset;S=F(),
while 1:S={F(F(u*((w:=len(Q)*z-sum(Q))-m*w.real)+(z*z).real%2/2for z in Q)for m in(0,2)for u in U):Q for P in S for Q in{P|{z+d}for z in P or{0,1}for d in U}-{P}}.values();print(len(S))
