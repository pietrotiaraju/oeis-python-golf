S={n:=1}
while[{n-a-b for a in S for b in S}&S or S&{n-a for a in S|{0}}and print(n)]:n+=1;S|={n*n}
