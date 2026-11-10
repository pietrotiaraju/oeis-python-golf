g=lambda E,x=0,*U:x<1 or sum(g(E|{y-x,v+x-y,(x+y)%-v},*[u for u in U if u-y])for y in U if not{y-x,(x+y)%-v}&E)
v=3
while[print(g({0},*range(1,v)))]:v+=2
