# A001598

> Number of terms in {b(1)..b(n)} relatively prime to b(n), where b(n) = A001597(n).
> — [OEIS A001598](https://oeis.org/A001598)

Offset 1: 1, 1, 1, 3, 2, 5, 5, 4, 2, 9, 5, 8, 5, 13, 12, 8, 5, 17, 8, 6, 11, 14, 11, 23, …

### Python 3 — 118 bytes

```python
from math import*
D={1:0};L=[];n=0
while 1:
 n+=1;m=D.pop(n,n);D[n*m]=m
 if m<n:L+=n,;print(sum(gcd(n,y)<2for y in L))
```

**How it works**

- The perfect powers b(1) = 1, b(2) = 4, … of [A001597](../A001597/) are
  found by walking through every integer n with a dict `D` that maps an
  upcoming power to its base. When n is in `D` with base m, n is a perfect
  power and its chain moves on to n·m. When n is not in `D`, it is not a
  perfect power, and `D.pop(n,n)` returns n itself, so `D[n*m]=m` starts
  the chain n², n³, … of the new base n.
- Only bases that are not perfect powers start chains, and their chains
  never meet: if rᵃ = sᵇ with r ≠ s, unique factorization makes r and s
  powers of a common base, so one of them is a perfect power. So every key
  of `D` comes from one chain, and the chains of these bases cover every
  perfect power, since each one is rᵏ (k ≥ 2) for a base r that is not a
  perfect power. 1 is put in by hand as `D={1:0}`: it pops base 0 < 1.
- `L` collects b(1), …, b(n), and the term counts those y with
  gcd(b(n), y) = 1. b(n) counts itself only when it is 1, which is right:
  a(1) = 1.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The dict keeps one entry per integer passed (a pending power for each
  base), so memory grows with b(n); the b-file ends at b(1000) = 804357,
  about 8·10⁵ steps and 150 MB, in about 2 s here. The bar is the whole
  b-file.
- Generating the powers block by block, as the
  [A001597](../A001597/) record does, and counting with the same `gcd` sum
  is 165 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 118 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001598), CC BY-SA 4.0.
