g=lambda P,k:k//n*(2-all(c-w+w%K*2in P for w in P if w%K<n-h)+2*({w%K*K+w//K for w in P}=={*P}))+sum(g(Q,k+1)for v in range(n)if k<h or v+P[k-h]%K==n-1for Q in[P+[K*k+v]]if len({a-b for a in Q for b in Q if(a-b)%K})==k*k+k)
n=1
while[K:=2*n,h:=n-n//2,c:=K*n-K+h,print((g([],0)+7)//8)]:n+=1