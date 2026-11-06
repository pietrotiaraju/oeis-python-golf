r=[0]
for n in r:r+=n+1,;B=3*n**n;print(sum((B+k)**n//B**k%B for k in r))
