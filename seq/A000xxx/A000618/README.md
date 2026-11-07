# A000618

> Number of nondegenerate Boolean functions of n variables: For n > 0, a(n) = A000616(n) - A000616(n-1).
> — [OEIS A000618](https://oeis.org/A000618)

Offset 0: 2, 1, 3, 16, 380, 1227756, 400507805615570, …

### Python 3 — 221 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(m:=2*lcm(*L))and 1<<sum(prod((t//(g:=gcd(t,l))%2*l<1)<<g for l in L)for t in range(m))//m
n=o=0
while[print(-o+(o:=f(n)))]:n+=1
```

**How it works**

- `f(n)` is [A000616](../A000616/)(n), the number of NP-equivalence classes
  of Boolean functions of n variables: Burnside's lemma over the signed
  permutations of the inputs, computed by a recursion over signed cycle
  types (see that page for the recursion, the fixed-point count of gᵗ and
  why every floor is exact).
- The program prints the running difference `-o+(o:=f(n))` with `o`
  starting at 0, so the first line is A000616(0) = 2, the OEIS value of
  a(0), and then A000616(n) − A000616(n−1) for n ≥ 1.

**Notes**

- All 9 b-file terms (n = 0 to 8) come out in well under a second; the bar is
  the whole b-file, 9 terms in 60 s. The recursion visits 2·3^(n−1) signed
  compositions, so later terms slow down by about 3 per step.
- From n = 14 the terms pass Python's 4300-digit limit for printing integers.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 221 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000618), CC BY-SA 4.0.
