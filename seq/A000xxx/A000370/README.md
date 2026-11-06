# A000370

> Number of NPN-equivalence classes of Boolean functions of n or fewer variables.
> — [OEIS A000370](https://oeis.org/A000370)

Offset 0: 1, 2, 4, 14, 222, 616126, 200253952527184, 263735716028826576482466871188128, …

### Python 3 — 235 bytes

```python
from itertools import*
n=0
while 1:
 t=k=0
 for*m,p in product(range(2**n),permutations(range(n))):
  r=b=1
  for w in p:m+=[y^1<<w for y in m]
  for x in m:
   while~x:b&=m[x]!=x;m[x],x=-1,m[x];r<<=x<0
  t+=r<<b;k+=2
 print(t//k);n+=1
```

**What is counted**

- Two functions {0,1}ⁿ → {0,1} are NPN-equivalent when one becomes the other
  by permuting the inputs, negating some inputs and possibly negating the
  output. A function of fewer than n variables is a function of n variables
  that ignores some of them, so "n or fewer" changes nothing: a(n) is the
  number of orbits of B_n × Z₂ on the 2^(2ⁿ) functions of n variables.
- Permuting and negating inputs is the group B_n of 2ⁿ·n! maps
  g(x) = P·x ⊕ s on the 2ⁿ points (P a permutation of the coordinates, s a
  mask). By Burnside's lemma,
  a(n) = Σ_g (fix(g) + fix(g·¬)) / (2·|B_n|).
- A function is fixed by g when it is constant on each cycle of g on the
  points, so fix(g) = 2^c(g), with c(g) the number of cycles. It is fixed by
  g·¬ when it alternates along every cycle, which needs every cycle to have
  even length; then there are again 2^c(g) such functions.
- So a(n) = Σ_g 2^c(g)·(2 if all cycles of g are even, else 1) / (2·|B_n|).
  This is twice [A000157](../A000157/), whose program is the same sum
  divided by 4·|B_n|.

**Odd cycle ⟺ fixed point**

The program never measures cycle lengths. For g in B_n, some cycle has odd
length exactly when g has a fixed point. A fixed point is a cycle of length
1. Conversely, if x lies on a cycle of odd length L, let
u = x ⊕ g(x) ⊕ … ⊕ g^(L−1)(x). An affine map over GF(2) commutes with sums of
an odd number of terms, so g(u) = g(x) ⊕ … ⊕ g^L(x) = u, and u is a fixed
point.

**How it works**

- `for*m,p in product(…)` runs over every mask s and permutation p; the
  starred target makes `m` the one-element list `[s]`.
- `for w in p:m+=[y^1<<w for y in m]` doubles the list once per coordinate,
  so that `m[x]` = s ⊕ (bit i of x moved to bit p[i]): `m` is g as a
  permutation of `range(2**n)`. For n = 0 the loop is empty and `m = [0]` is
  the identity on the single point.
- `for x in m` reads each position in turn. If it was already visited it
  reads −1 and skips; otherwise it reads a point of an unvisited cycle and
  walks it, marking every point −1. The step that lands on a marked point
  sets x to −1, ends the walk and doubles `r`, so `r` ends at 2^c(g). On the
  way `b&=m[x]!=x` clears `b` at a fixed point, and `r<<b` is
  2^c(g)·(2 or 1).
- `k` grows by 2 per group element, so `t//k` = Σ_g 2^c(g)·(2 or 1) / (2·|B_n|).
- n = 0 needs no special case: the one map has one cycle, a fixed point, and
  weight 2, so the first line is 2//2 = 1.

**Notes**

- The program walks all 2ⁿ·n! elements on 2ⁿ points: it prints 7 terms
  (n = 0 to 6) in about 5 s, and the eighth, 645 120 elements on 128 points,
  takes well over a minute. The bar is 7 terms in 60 s; the b-file has 12
  (n = 0 to 11).
- It is the [A000157](../A000157/) frame with the cycle walk of
  [A000214](../A000214/): testing x itself, which becomes −1 exactly when
  the cycle closes, instead of `~m[x]` and `m[x]<0`.
- `r=b=1` has its own line because for n = 0 the doubling loop never runs:
  resetting it there, as A000157 does, would need `r=b=1;` before the main
  loop as well (4 bytes more).
- Reading s and the coordinate images off the digits of one integer, as
  A000214 does (`for i in range((N:=2**n)*n**n)`, keeping only the
  bijections), is 230 bytes without the import, but it visits all n^n
  digit strings: n = 6 alone takes minutes, so it does not reach the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 235 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000370), CC BY-SA 4.0.
