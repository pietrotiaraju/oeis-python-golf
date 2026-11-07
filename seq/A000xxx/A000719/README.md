# A000719

> Number of disconnected graphs with n nodes.
> — [OEIS A000719](https://oeis.org/A000719)

Offset 0: 0, 0, 1, 2, 5, 13, 44, 191, 1229, 13588, 288597, 12297299, 1031342116, 166123498733, …

### Python 3 — 213 bytes

```python
import math
f=lambda r,*L:r<1or sum(f(r+k,*L,k)<<-k//2+sum(map(math.gcd,L,[k]*n))for k in range(-r,0))//r
R=1,;C=[0];n=s=0
while[print(s)]:R=f(n:=n+1),*R;s=sum(d*C[d]*sum(R[d::d])for d in range(1,n))//n;C+=R[0]-s,
```

**How it works**

- a(n) = g(n) − c(n), all graphs minus connected graphs on n unlabeled
  nodes. `f(n)` is g(n) ([A000088](../A000088/)), counted by Burnside's
  lemma one cycle at a time, divided by r at each level, without the cache
  of the A000088 record.
- A graph is a multiset of connected graphs, so G(x) = Π_d (1 − x^d)^(−c(d))
  (Euler transform). Taking x·G′/G and comparing coefficients:
  n·g(n) = Σ_{d=1..n} d·c(d)·Σ_{j≥1} g(n − dj). The term d = n is n·c(n),
  so n·a(n) = n·(g(n) − c(n)) is the same sum over d < n, and no Möbius
  function is needed (the inverse Euler transform used in
  [A000282](../A000282/)).
- `R` is the tuple g(n), g(n−1), …, g(0), newest first, so the inner sum
  Σ_j g(n − dj) is `sum(R[d::d])`. `C` holds c(d) (C[0] is a placeholder),
  and `C+=R[0]-s,` stores c(n) = g(n) − a(n) once a(n) is known.
- `R=f(n:=n+1),*R` bumps n and prepends g(n) in one statement; a(0) = 0 is
  the initial `s`.

**Notes**

- Exact integer arithmetic: the sum is exactly n·a(n), so `//n` is exact.
- The uncached recursion visits all 2^(n−1) compositions of n: about 23
  terms in 60 s on the PC used (a(22) at about 32 s). The bar is 18 terms in
  60 s; the b-file has 88.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 213 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000719), CC BY-SA 4.0.
