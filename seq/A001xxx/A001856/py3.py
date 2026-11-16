l=[1];S={r:=0}
for x in l:
 print(x);S|={x-y for y in l}
 while r in S:r+=1
 l+=x+(x,r)[len(l)%2],
