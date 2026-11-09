c=[0]
exec('c+=[x^5574*len(c)^1for x in c];'*12)
for k in range(7):print(sum(x.bit_count()==4*k for x in c))
