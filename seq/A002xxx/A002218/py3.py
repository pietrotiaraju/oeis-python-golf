from math import*
P=[0,1];N=1
def F(L,Q,m):
 S[:]=map(int.__add__,S,Q+[L.count(1)*Q[N]])
 for k in range(m,N+1-sum(L)):e=k//2+sum(gcd(k,j)for j in L);F(L+[k],[(sum(Q[i-k*j]*P[j]for j in range(i//k+1))<<e)//k//-~L.count(k)for i in range(N+1)],k)
def l(h):
 d=[0];a=[1]
 for n in range(1,len(h)):d+=(n*h[n]-sum(d[j]*h[n-j]for j in range(n)))//h[0],;a+=(d[n]-sum(j*a[j]for j in range(1,n)if n%j<1))//n,
 return a
while 1:N+=1;P+=0,;S=[0]*N*2;K=perm(N);F([],[K]+[0]*N,1);P[N]=(S[N-1]-S[N+1])//K;print(l(S)[N-1]-l(P[1:])[N-2])
