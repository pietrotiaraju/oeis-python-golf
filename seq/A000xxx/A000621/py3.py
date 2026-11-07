A=1,
while[print(A[-1])]:A+=sum(map(int.__mul__,A,A[::-2])),
