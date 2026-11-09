s=1
for n in range(129):s|=s<<n*n;s>>n&1or print(n)
