S={b'13'*3};n=p=k=0
while[n<6or print(sum((x in(x+x)[1:-1]+b'.'+x[::-1]*2)<1>len({p for c in x if c%3*[p:=p+1j**(k%6//1.5),k:=k+c]})-n for x in S))]:n+=1;S={min(r[j:]+r[:j]for r in(v,v[::-1])for j in range(9*n))for w in S for i,c in enumerate(w)if c&2for v in[w[:i]+b'13131'+w[i+1:]]}
