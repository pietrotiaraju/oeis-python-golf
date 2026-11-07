n=0
while r:=range(n,1-n):print(sum(x*x+y*y+z*z<=n*n for x in r for y in r for z in r));n-=1
