R=[1,1]
while[print(R[1])]:R=[~-len(R)*sum(map(int.__mul__,R,R[-2::-1]))]+R
