f=lambda F,k:max([f(F+[v],k+1)for v in{(F[a]+F[k//a])%d for a in range(2,k)if k%a<1}or range(d)if v-F[-1]and v+F[0]*~-k//4&1<=d%(2*k)]+[k-1])
n=2
while[print(max(f([D,0],2)for D in range(2*n)if n%(d:=n-D%n)<1))]:n+=1
