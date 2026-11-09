P=lambda v,s=0:[s:=s+x for x in[0]+v]
S=lambda W:[P([*map(sum,zip(*W))][::-1]),*map(P,W[:-1])]
A=[[0],[2]];B=[[-2]]
while[print(sum(map(sum,A+B)))]:A=S(A);B=S(B)
