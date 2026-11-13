import math
a=[0,1];m=0
while[print(a[m])]:m+=1;a+=a[m]-sum(math.comb(m,k)*a[k]*a[-k]for k in range(m)),
