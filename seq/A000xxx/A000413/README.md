# A000413

> Let A(n) = #{(i,j,k): i^2 + j^2 + k^2 <= n}, V(n) = (4/3)*Pi*n^(3/2), P(n) = A(n) - V(n); A000092 gives values of n where |P(n)| sets a new record; sequence gives A(A000092(n)).
> — [OEIS A000413](https://oeis.org/A000413)

Offset 0: 1, 7, 19, 57, 81, 251, 437, 691, 739, 1743, …

### Python 3 — 302 bytes

```python
from math import*
s=lambda t,d=3:t and t+s(t*~-d//4//d,d+2)
A=lambda n:sum(2*isqrt(n-a-b)+1for a in Q for b in Q if a+b<=n)
X=lambda n:G*A(n)-s(n*isqrt(12*n*G*G))
p=n=0;Q=[0];G=8**8
print(1)
while Q:=Q+[n:=n+1,n]*(isqrt(n)**2==n):
 while abs(d:=abs(X(n))-abs(X(p)))<n*isqrt(G):G*=2
 0<d==print(A(p:=n))
```

**How it works**

Use the exact lattice-point and record-comparison algorithm of
[A000092](../A000092/). Q stores one zero square and two copies
of every positive square through n, representing both signs.
A(n)=sum(2*isqrt(n-a-b)+1,a,b in Q,a+b<=n) therefore counts
all integer triples in the ball. X is a scaled interval estimate
of A(n)-(4/3)*pi*n^(3/2), using the convergent arcsine series
proved and bounded on A000092. Double the scale until the
record comparison is separated from zero by n*isqrt(G);
for G>=2^24 this is larger than the combined error bounds.
For distinct n the true absolute-error gap is nonzero, since
otherwise pi times a nonzero algebraic number would be an integer.
Thus each comparison resolves. Print the exact A(n) at every
record, and prepend A(0)=1 for this entry's offset 0.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 31 terms in 20 s; the official b-file contains 43 terms.
- The bar includes the origin and the first 30 positive-radius records, matching the established A000092 verification range. Runtime grows with the record radii; no fixed numerical precision is assumed.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 302 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000413), CC BY-SA 4.0.
