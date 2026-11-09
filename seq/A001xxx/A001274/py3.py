D={};a=k=1
while 1:
 b=k=k+1
 for p in D.pop(k,[k]):b-=b//p;D[k+p]=D.get(k+p,[])+[p]
 a-b or print(k-1);a=b
