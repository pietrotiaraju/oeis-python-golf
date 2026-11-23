p=lambda n,m=1:{B**n}|{B**k+q for k in range(m,n)for q in p(n-k,k)}
B=0
while 1:B+=5;E=S=p(B//5);exec("S={s+e for s in S for e in E};"*3);print(len(S))
