n=1
while R:=range(n):print(len({2*x*x+5*y*y-1for x in R for y in R}&{*R}));n*=2
