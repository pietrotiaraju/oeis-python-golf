f=lambda r,c,S:r//n or sum(f(r+-~c//n,-~c%n,S|T)for x in[r+c][r*c:]or range(n)if not(T:={(r,x),(~c,x)})&S)
n=1
while[print(f(0,0,{0}))]:n+=1
