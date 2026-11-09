f=lambda p,u,i=0:sum(f([v]+p,u-{v},i+1)for v in u-{i}if min((p[0]-x)*(v-x)for x in[p,u][i%2])>=v-i&1)if u else([p[p[k]]for k in p]==p)+1
n=3
while[print(f([n],{*range(n)})//4)]:n+=2
