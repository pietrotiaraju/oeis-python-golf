# A001152

> Number of n-input 3-output switching networks with GL(n,2) acting on the input and S(3) and C(2,3) acting on the output.
> — [OEIS A001152](https://oeis.org/A001152)

Offset 1: 4, 36, 3178, 298908192, 165073828103027338592, …

### Python 3 — 255 bytes

```python
n=1
while 1:
 t=k=0
 for i in range(1<<n*n):
  for _ in[m:=[0]]*n:m+=[y^i%2**n for y in m];i>>=n
  r=len({*m})>>n;k+=r;u=v=w=r
  for x in m:
   L=-1
   while~x:m[x],x=-1,m[x];L+=1
   if~L:u*=8;v<<=1+2*(L%3<1);w<<=3-L%2
  t+=u+8*v+6*w
 print(t//k//48);n+=1
```

**How it works**

- Burnside's lemma. A network is a map f: GF(2)ⁿ → GF(2)³, and the group is
  GL(n,2) on the inputs times the 48 symmetries of the output cube (S(3)
  permutes the outputs, C(2,3) complements them). A pair (A, h) fixes f when
  f(Ax) = h(f(x)) for all x. Along a cycle of A of length L, f is fixed by its
  value at one point, which must be a fixed point of h^L. So (A, h) fixes
  Π_cycles fix(h^L) maps.
- A fixes the zero vector, so only the 15 output symmetries with a fixed
  vertex count (the others give a factor 0 from that 1-cycle):
  - the identity, with fix(h^L) = 8;
  - 8 rotations about a body diagonal (two fixed vertices and two 3-cycles),
    with fix(h^L) = 8 when 3 | L and 2 otherwise;
  - 6 reflections in a plane through two opposite edges (four fixed vertices
    and two 2-cycles), with fix(h^L) = 8 when 2 | L and 4 otherwise.
  So a(n) = Σ_A (Π 8 + 8·Π(2 or 8) + 6·Π(4 or 8)) / (48·|GL(n,2)|).
- `i` runs over all n×n matrices. `m` starts as [0] and each n-bit column c
  doubles it with `y^c`, so m[x] is the image of x. A is invertible exactly
  when the 2ⁿ images are distinct; then `r=len({*m})>>n` is 1, and otherwise
  0, which zeroes u, v and w and keeps A out of the count `k = |GL(n,2)|`.
- The cycle walk marks each visited point with −1. Starting from the image
  of an unvisited point it takes L + 1 steps around a cycle of length L, and
  from a visited one none, so `L` (started at −1) is the cycle length, or −1
  when there is no new cycle. Each cycle multiplies u by 8, v by 2 or 8
  (`<<1` or `<<3`) and w by 4 or 8 (`<<3-L%2`).

**Notes**

- Exact for every n: integer arithmetic only; the division is exact by
  Burnside.
- The run is over all 2^(n²) matrices: a(4) arrives in about 2 s, but a(5)
  needs 2²⁵ matrices, far past 60 s. The bar is 4 of the 6 b-file terms in
  60 s.
- Harrison's companion counts on this site: the same output group with S(n)
  on the inputs, [A000857](../../A000xxx/A000857/), and GL(n,2) with only the
  complements on the outputs, [A000848](../../A000xxx/A000848/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 255 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001152), CC BY-SA 4.0.
