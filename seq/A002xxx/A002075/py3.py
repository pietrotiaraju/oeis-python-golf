import math
L=[0];n=0
while 1:n+=1;L+=sum(3**(g:=math.gcd(k,n))*(6-(d:=n//g)*-d%6)+d%2*3-n*L[k]*(g==k)for k in range(n))//n,;print(L[n]//6)
