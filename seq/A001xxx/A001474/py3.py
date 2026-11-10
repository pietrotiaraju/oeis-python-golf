import math
w=1
while[any(w**3==x**3+y**3+z**3for x in range(w)for y in range(x)if math.gcd(w,x,y)<2for z in range(-y,y))and print(w)]:w+=1
