D={};k=0
while 1:
 k+=1;L=D.pop(k,[])+[k]
 for d in L:D[k+d]=D.get(k+d,[])+[d]
 k*len(L)%sum(L)or print(k)
