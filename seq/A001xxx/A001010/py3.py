A=[()];B=[[0]]
while[print(len(B))]:A,B=B,[(a-~a,*[w*2for w in q],~a-a)for q in A for a in{0,*q,-len(A)}for p,*r in[(*q,-a)]if all((a<c)^(a<d)==(p<c)^(p<d)for c,d in zip(*[iter(r)]*2))]
