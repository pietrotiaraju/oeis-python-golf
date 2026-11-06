M=[0,1]
while[print(len(M))]:M=[a-b*~M[-1]for b in M for a in M if a&~b<1]
