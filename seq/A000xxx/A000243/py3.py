r=s=[n:=1]
while[print(v:=sum(map(int.__mul__,r,s)))]:r+=sum(-~j*r[j]*sum(r[~j::~j])for j in range(n))//n,;s=[v+r[n]]+s;n+=1
