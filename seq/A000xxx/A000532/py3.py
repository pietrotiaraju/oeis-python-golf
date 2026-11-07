f=lambda v,R:sum(f(u,R-{u})for u in{v+1,v-1,v-~n,v+~n}&R)or not R
n=1
while[print(f(-1,{x+x//n for x in range(n*n+1)}))]:n+=1
