L=[0]*3;m=2
while m:=m+1:L+=m*~-m*(m-2)//6-sum(L[d]for d in range(m)if-~m%-~d<1),;print(L[m])
