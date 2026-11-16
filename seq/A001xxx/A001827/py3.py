from math import*
n=0
while[print(sum(comb(n,t)*comb(t,q)*(2**q+2**t)**(n-t)for t in range(n+1)for q in range(t+1)))]:n+=1
