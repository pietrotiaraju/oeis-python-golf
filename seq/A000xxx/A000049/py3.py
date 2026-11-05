n=0
while 1:r=range(2<<n//2);print(len({min(3*x*x+4*y*y,2**n+1)for x in r for y in r})-2);n+=1
