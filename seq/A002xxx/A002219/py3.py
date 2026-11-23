p=lambda n,m=1:{B**n}|{B**k+q for k in range(m,n)for q in p(n-k,k)}
B=0
while 1:B+=3;E=p(B//3);print(len({a+b for a in E for b in E}))
