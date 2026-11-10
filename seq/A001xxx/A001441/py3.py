g=lambda P,k:k//n*3**({w%K*K+w//K for w in P}=={*P})+sum(g(Q,k+1)for v in range(n)for Q in[P+[K*k+v]]if len({a-b for a in Q for b in Q if(a-b)%K})==k*k+k)
n=1
while[K:=2*n,print((g([],0)+7)//8)]:n+=1