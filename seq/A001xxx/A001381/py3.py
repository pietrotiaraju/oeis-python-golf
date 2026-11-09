c=[0]
exec('c+=[x^9205487*len(c)for x in c];'*12)
w=[-~(x^y<<12).bit_count()//2for x in c for y in c]
for k in range(13):print(w.count(2*k))
