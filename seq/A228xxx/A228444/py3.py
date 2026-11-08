g=lambda m,e=0:m+sum(e*d or-g(d)for d in range(1,m)if m%d<1)
n=1
while[g(p:=int(f"{g(g(n,1))}{g(g(n),1)}"))>p-2!=print(p)]:n+=1
