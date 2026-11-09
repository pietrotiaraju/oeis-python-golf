C={0};L={}
for i in range(12):C|={c^6378<<i^1for c in C};L[95%2**i]=0
[b>a or print(sum(c&a^b|(c&916384).bit_count()^2<1for c in C))for a in L for b in L]
