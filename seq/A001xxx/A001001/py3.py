r=[1]
for n in r:r+=n+1,;print(sum(d*e for e in r for d in r[e-1::e]if n%d<1))
