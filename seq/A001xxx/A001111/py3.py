B=int.bit_count
C=lambda U,T,P:next((q for b in U if[r:=0]+[r:=r<<B(c)|2**B(b&c)-1for c in P]and(q:=2*(r<T[0])or r==T[0]and C([u for u in U if u-b],T[1:],[x for c in P for x in(c&~b,c&b)if x]))>(U==T)),[]==T)
G=lambda R,S,D,d=0:(d%v>6or C(R,R,[2**v-1])<2)and sum((G(R+[x],[y for y in S if B(x&y)-v//4==0<y-x],D|x*2^x,d+1)for x in S if x&~(x*2|D)<1),d==v)
v=3
while[print(G([],[x for x in range(2**v)if B(x)==v//2],1))]:v+=4
