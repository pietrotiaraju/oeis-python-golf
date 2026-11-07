A=1,
while[print(sum(map(int.__mul__,A[1:],A[-3:0:-2])))]:A+=sum(map(int.__mul__,A,A[::-2])),
