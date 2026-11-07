from math import*
R=[n:=1];B=[]
while[print(R[0])]:B+=sum((-1)**(n+(g:=gcd(j,n)))*comb(2*g-1,g)for j in range(n))//n,;R=[sumprod(B,R)//n]+R;n+=1
