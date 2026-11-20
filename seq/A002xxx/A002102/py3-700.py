S={0};n=0
while[print(sum(n-x-y in S for x in S for y in S))]:n+=1;S|={n*n}
