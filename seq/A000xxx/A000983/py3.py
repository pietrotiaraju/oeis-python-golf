P=[0,1];k=1
f=lambda U,k:not U or k*len(P)>=len(U)and any(f(U-{w^i^j for j in P},k-1)for w in[min(U)]for i in P)
while 1:
 if f({*range(2*P[-1])},k):print(k);P+=2*P[-1],
 else:k+=1
