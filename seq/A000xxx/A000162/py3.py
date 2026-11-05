F=lambda o:(t:=o|{r for q in o for r in zip(*[((y,z,x),(-y,x,z))for x,y,z in q])})>o and F(t)or o
s={((0,)*3,)}
while[print(len(s))]:s={(*min(sorted((x-a,y-b,z-c)for x,y,z in r)for r in F({q+(u,)})for a,b,c in[min(r)]),)for q in F(s)for x,y,z in q if(u:=(x+1,y,z))not in q}
