f=lambda r,c,S,p:sum(f(r+-~c//n,-~c%n,S|T,p+len({(r*r,y)for y in range(x,n)}&S))for x in[r+c][r*c:]or range(n)if not(T:={(r,x),(~c,x)})&S)if r<n else p&1
n=1
while[print(f(0,0,{0},n>1))]:n+=1
