# A000666

> Number of symmetric relations on n nodes.
> — [OEIS A000666](https://oeis.org/A000666)

Offset 0: 1, 2, 6, 20, 90, 544, 5096, 79264, 2208612, 113743760, 10926227136, 1956363435360, …

### Python 3 — 135 bytes

```python
import math
f=lambda r,*L:r<1or sum(f(r-k,*L,k)<<k//2-~sum(map(math.gcd,L,[k]*n))for k in range(1,r+1))//r
n=0
while[print(+f(n))]:n+=1
```

**How it works**

- This is the [A000250](../A000250/) program without its final halving:
  A000250(n) = A000666(n)/2, and that page shows that `f(n)` is A000666(n).
- Burnside's lemma over S_n acting on the C(n + 1, 2) unordered pairs
  {x, y} with x = y allowed: a cycle of length k has ⌊k/2⌋ + 1 orbits of
  its own pairs (⌊k/2⌋ edge orbits and one loop orbit), and two cycles of
  lengths k and l have gcd(k, l) orbits between them. `f(r,*L)` recurses on
  the cycle through one of the r remaining points and adds
  `k//2-~sum(map(math.gcd,L,[k]*n))` = ⌊k/2⌋ + 1 + Σ gcd(k, l) orbits to
  the exponent; dividing by r at every level is exact by de Bruijn's lemma.
- The offset starts at n = 0, where `r<1or` returns `True`; the `+` prints
  it as 1. A000250 instead starts at 1 and prints `f(n)>>1`.

**Notes**

- 2^(n−1) compositions: 23 terms in about 40 s here. a(n) has a little
  under 0.15·n² digits, so Python's 4300-digit int-to-str limit would only
  stop the output at n = 175.
- The bar is 18 terms in 60 s, as for A000250; the b-file has 81.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 135 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000666), CC BY-SA 4.0.
