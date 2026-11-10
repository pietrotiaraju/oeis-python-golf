m=0
while[t:=1,m:=m+1]:
 for k in range(m):print(t);t=t*(m+k)*(m+~k)//2//-~k
