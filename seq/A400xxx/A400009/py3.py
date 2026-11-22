from functools import*
@cache
def g(s):return min({*range(len(s)+1)}-{g((*filter(x.__rmod__,s),))for x in s})
s=()
while[print(g(s))]:s+=len(s)+2,
