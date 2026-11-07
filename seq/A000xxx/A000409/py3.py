import math
s=[1,-1];n=1
while 1:n+=1;s=[a-n*b for a,b in zip([0]+s,s+[0])];print(sum(s[k]*math.comb(2**k-1,n)for k in range(n)))
