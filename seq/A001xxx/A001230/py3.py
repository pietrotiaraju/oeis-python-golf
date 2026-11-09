g=lambda p,S:all(len(N[w]&S)>1for w in S-{p,0})and sum(g(q,S-{p})for q in N[p]&S)or{0}==S
n=2
while 1:V={x%n+x//n*1j for x in range(n*n)};N={p:{q for q in V if abs(p-q)==5**.5}for p in V};print(+g(1+2j,V));n+=2
