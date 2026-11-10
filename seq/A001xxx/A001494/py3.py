D={};a=b=0;k=1
while 1:
 c=k=k+1
 for p in D.pop(k,[k]):c-=c//p;D[k+p]=D.get(k+p,[])+[p]
 a-c or print(k-2);a,b=b,c
