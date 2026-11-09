print('0\n1');D={0:1,1:0}
while[print(sum(h&a&D[a]==h for a in D for h in D))]:D={a|b*-~D[0]:D[b]|D[a]*-~D[0]for a in D for b in D if a&~b<1}
