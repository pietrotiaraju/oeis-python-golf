n=O=1;F=2
while 1:
 if O==n:print(F);n+=1;B=[(0,1),(1,0)]
 u,v=map(sum,zip(*B));F=p=1;O=0
 while(p:=p+1)**u<2**v:
  k=F%p>0
  while(k+1)**v>p**u*k**v>0:k+=1;F*=p;O+=1
 B[O<n]=u,v
