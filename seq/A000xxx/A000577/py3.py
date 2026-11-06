def c(S,k=5):
 a,b,t=map(min,zip(*S));T=tuple(sorted((x-a,y-b,t)for x,y,t in S))
 return min(T,tuple(sorted((y,x,t)for x,y,t in T)),k and c([(-y-1,x+y+t,1-t)for x,y,t in S],k-1)or T)
L={((0,0,0),)}
while[print(len(L))]:L={c((*S,u))for S in L for x,y,t in S for a,b in((0,0),(1,0),(0,1))if(u:=(x+a*(2*t-1),y+b*(2*t-1),1-t))not in S}
