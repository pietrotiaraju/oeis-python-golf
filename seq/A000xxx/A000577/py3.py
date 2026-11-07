L={((0,1,0),)}
while[print(len(L))]:L={min(tuple(sorted((x-a,t,y-b)[::d]for x,t,y in R))for k in S*6if[R:=[(-y,-t,x+y-t)for x,t,y in R]]for a,_,b in R for d in(1,-1))for S in L for x,t,y in S for k in(1,2,3)if{*S}<(R:={*S,(x-k//2*t,-t,y-k%2*t)})}
