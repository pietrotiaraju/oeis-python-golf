n=0
while 1:r=range(2<<n//2);print(len({min(x*x+2*y*y,2**n)for x in r for y in r})-1);n+=1
