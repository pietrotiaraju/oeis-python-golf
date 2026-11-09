C={0};L={}
for i in range(12):C|={c^6378<<i^1for c in C};L[76377%4**i]=0
[b>a or print(sum(c&a^b==12-c.bit_count()for c in C))for a in L for b in L]
