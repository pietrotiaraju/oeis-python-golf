D={};x=y=k=1
while 1:
 b=k=k+1
 for p in D.pop(k,[k]):b-=b//p;D[k+p]=D.get(k+p,[])+[p]
 b-x-2or print(k-2);x,y=y,b
