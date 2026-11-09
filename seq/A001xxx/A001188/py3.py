from math import*
r=[s:=1];G=[1];C=[]
while 1:n=len(C);C+=s*s-sum(comb(n,i)*C[i]*G[n-i]for i in range(n)),;G+=s*s,;r=[s]+[s:=s+x for x in r];print(C[-1]+1>>1)
