R=[n:=1]
while[print(R[-1])]:R+=2*sum(-~j*R[j]*sum(R[~j::~j])for j in range(n))//n,;n+=1
