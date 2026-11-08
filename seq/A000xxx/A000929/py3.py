f=lambda n,k=1:n>=k and f(n-k,k)+f(n,k-~k)or n<1
n=0
while[print(+f(n))]:n+=1
