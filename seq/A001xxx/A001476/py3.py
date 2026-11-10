s=1
for n in range(12759):s|=s<<n**3*(n<24);s>>n&1or print(n)
