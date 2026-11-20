a=[1];*P,F,n=1,1
while 1:P+=F%n*[n];F*=n*n;a+=sum(p*q*sum(a[-p*q::-p*q])for p in P for q in P if p<q)//n,;print(a[-1]);n+=1
