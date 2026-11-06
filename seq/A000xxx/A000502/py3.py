from math import*
n=5
while 1:print(comb(n,4)*(2*(64*n*n+432*n+83)*4**(n-4)-(2*n+1)**2*comb(2*n,n))//30);n+=1
