L=[0]*4;m=3
while m:=m+1:L+=m*~-m*(m-2)*(m-3)//24-sum(L[d]for d in range(m)if-~m%-~d<1),;print(L[m])
