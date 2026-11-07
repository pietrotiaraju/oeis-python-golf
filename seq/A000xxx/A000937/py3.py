P=[1]
g=lambda v,F,B:max([w in P or-~g(w,F|N,B|2*w)for N in[{v^j for j in P}]for w in N-F if w<=B]+[1-B])
for j in P:print(g(1,{0},3)+2);P+=2*j,
