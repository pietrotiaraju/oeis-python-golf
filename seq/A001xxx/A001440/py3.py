g=lambda P,i=-1,*U:i<0 or sum(g(Q,*[u for u in U if u-j])for j in(i,*U)for Q in[{*P,K*i+j,K*j+i}]if len({a-b for a in Q for b in Q})>len(Q)*~-len(Q))
n=1
while[K:=2*n,print(g((),*range(n))+1>>1)]:n+=1
