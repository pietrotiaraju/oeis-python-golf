R=[n:=1];v=[2]
while[print(v[-1]-1//n)]:v+=sum(map(int.__mul__,R:=[sum(R+[j*R[~j]*sum(R[j-1::j])for j in range(1,n)])//n]+R,v)),;n+=1
