f=lambda n:len({*(s:=b'%d'%n)})>1and-~f(int(bytes(48+abs(a-b)for a,b in zip(s,s[1:]+s))))
n=1
while[print(+f(n))]:n+=1
