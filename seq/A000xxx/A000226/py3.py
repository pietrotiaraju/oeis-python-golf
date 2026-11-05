R=[n:=1]
while[print(sum((R[a]+(a==b))*(R[b]+2*(n+~a==b+b))*R[~a-b]for a in range(n)for b in range(n-a))//6)]:R+=sum(-~j*R[j]*sum(R[~j::~j])for j in range(n))//n,;n+=1
