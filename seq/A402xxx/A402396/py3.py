from itertools import*
Q=[sum(1<<int(str(a),3)for a in s)for k in(3,4)for s in combinations([i for i in range(223)if'3'>max(str(i))],k)if(W:=sum(d for a in s for d in b'\1\nd'if a+d in s))%9==~-k and'1'in str(W)]
e={0:1}
while 1:
 print(e[0])
 for q in range(9):
  d,e=e,{0:0};W=[P>>q for P in Q if P&-P==1<<q]
  for m,c in d.items():
   for k in[m>>1]if m&1 else[(m|v)>>1 for v in W if v&m<1]:e[k]=e.get(k,0)+c
