import math
f=lambda n,k,L,w,d=1:n>=k and f(n,k+1,L,w)+f(n-k,k,L+[k],w//k//d<<sum(math.gcd(k,j)for j in L)+k//2,d+1)or 0**n*w
n=0;F=1
while[print(f(n,1,[],F)//F)]:n+=1;F*=n
