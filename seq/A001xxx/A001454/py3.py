u,v=2,6;c=r=5
while[print(v-c)]:r+=1;u,v=v,((10*r*r-38*r+33)*v-9*(r-3)**2*u)//r**2;c=c*(4*r-10)//~-r
