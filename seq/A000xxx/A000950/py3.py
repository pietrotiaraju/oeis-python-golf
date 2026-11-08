f=lambda m,p=1,h=4,c=1:sum(f(i:=m-j,j,h-1)*(c:=c*p*i//j)for j in range(1,m*h))or m<2
n=2
while[print(f(n))]:n+=1
