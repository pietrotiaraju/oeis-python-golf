f=lambda L,p,k,y:k and max(f([q:=s|q<<a for s in L],a,k-1,len(bin(q^q+1)))for a in range(p,y-2)if[q:=0])or y-4
n=1
while[print(f([1]*-~n,0,6,4))]:n+=1
