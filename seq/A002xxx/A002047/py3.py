f=lambda i,V,A:i>n or sum(f(i+1,V-{v},A-{i+v})for v in V if i+v in A)
n=0
while[print(f(-n,R:={*range(-n,n+1)},R))]:n+=1
