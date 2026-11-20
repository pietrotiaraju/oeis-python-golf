a=[1];*P,F,n=1,1
while[print(a[-1])]:P+=F%n*[n];F*=n*n;a+=sum(x*(q:=q*p)for p in P if(q:=p)for x in a[-p::-p])//n,;n+=1
