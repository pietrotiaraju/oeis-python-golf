f=lambda n,j=1,s=0,F=1:s-n>2if j>n else f(n-j,j,s|F%j+1,F)+f(n,j+1,s,F*j*j)
n=1
while[print(f(n))]:n+=1
