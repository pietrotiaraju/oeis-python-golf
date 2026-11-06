Q=[[s:=1]]*3
while[print(s)]:s=0;Q=[[s:=s+i*e for i,e in enumerate([0]+E)]for E in Q]