R=[n:=1]
while[print(2*(Q:=sum(R[i]<<3*n*i for i in range(n)))*pow(2-Q,-3,M:=8**n**2)%M>>3*n*~-n)]:R+=sum(R+[d*R[d]*sum(R[-d::-d])for d in range(1,n)])//n,;n+=1
