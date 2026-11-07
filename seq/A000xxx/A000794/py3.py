import math
print('1\n2')
n=2
while 1:
 p=2;a=K=0;M=n**3;v=n*n+n+1
 while n%p:p+=1
 while p**K<M:K+=1
 for c in range(M*(p**K==M)):s=[1]*K;exec('s+=sum(c//p**i%p*s[i-K]for i in range(K))%p,;'*M);a=a or len({(*s[t:t+K],)for t in range(M)})>M-2!=(R:=[sum((any(s[d::v])<1)<<(i+d)%v for d in range(v))for i in range(v)])and sum((-1)**T.bit_count()*math.prod((~T&r).bit_count()for r in R)for T in range(2**v))
 print(a);n+=1
