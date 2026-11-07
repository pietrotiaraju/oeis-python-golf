f=lambda R,t:t<0 or any(f(R+[r],t-1)for x in range(1<<t)for r in[[s[~t]for s in R]+[0]+[x>>j&1or-1for j in range(t)]]if all(sum(map(int.__mul__,r,s))==0for s in R))
n=2
while 1:f([],n-1)and print(n);n+=4
