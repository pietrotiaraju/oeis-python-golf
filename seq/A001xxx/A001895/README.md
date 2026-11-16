# A001895

> Number of rooted planar 2-trees with n nodes.
> — [OEIS A001895](https://oeis.org/A001895)

Offset 1: 1, 2, 4, 12, 34, 111, 360, 1226, 4206, 14728, 52024, 185824, 668676, …

### Python 3 — 84 bytes

```python
c=[1,1,2];n=1
while[print((c[-1]+(3-n%2)*c[n//2])//4)]:c+=c[-1]*(4*n+6)//(n+3),;n+=1
```

**How it works**

- Harary and Palmer (*Graphical Enumeration*, 1973, (3.5.28)) give the
  generating function of rooted planar 2-trees,
  Σ a(n)xⁿ = (4 − 8x² − √(1 − 4x) − (3 + 2x)·√(1 − 4x²))/(8x²).
- √(1 − 4x) = 1 − 2Σ_{m≥1} C(m−1)·xᵐ with Catalan numbers C, and
  √(1 − 4x²) is the same series in x². Reading off x^(n+2) for n ≥ 1:
  a(n) = (C(n+1) + 3C(n/2))/4 for even n and (C(n+1) + 2C((n−1)/2))/4 for
  odd n, that is a(n) = (C(n+1) + (3 − n mod 2)·C(⌊n/2⌋))/4.
- The list `c` holds C(0)…C(n+1) and grows by one Catalan number per term
  with C(m+1) = C(m)·2(2m+1)/(m+2), here with m = n + 1; the division is
  exact. `c[-1]` is C(n+1) and `c[n//2]` is C(⌊n/2⌋).

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 200 terms (n = 1 to 200); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001895), CC BY-SA 4.0.
