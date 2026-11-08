f=lambda r,c,S:r//k or sum(f(r+-~c//n,-~c%n,S|T)for x in[r+c][r*c:]or range(n)if not(T:={(r,x),(~c,x)})&S)
n=k=1
while[print(f(0,0,{0}))]:k=k%n+1;n+=k<2
