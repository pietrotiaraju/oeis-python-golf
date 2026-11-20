from math import*
L=1,;T=[1];u=[0];r=[1];n=0
while 1:L+=(g:=sumprod(L,L[::-1])+L[3*n]>>1)+L[3*n],;L+=*[0]*4,(sumprod(L,L[::-1])+2*L[2*n])//6;n+=1;T+=g,;u+=n*g+sumprod(T[1:],u[::-1]),;r+=sumprod(T,T[::-1])+sumprod(T[1:n//2+1],r[-2::-2]),;print((sum(u[gcd(j,n)]for j in range(n))*2//n+r[n])//4-g)
