# A000350

> Numbers m such that Fibonacci(m) ends with m.
> — [OEIS A000350](https://oeis.org/A000350)

Offset 1: 0, 1, 5, 25, 29, 41, 49, 61, 65, 85, 89, 101, 125, 145, 149, …

### Python 3 — 62 bytes

```python
a=m=0;b=1
while[a%10**len(str(m))==m==print(m)]:a,b=b,a+b;m+=1
```

**How it works**

- a = F(m) and b = F(m + 1) step along with m, as exact big integers.
- F(m) ends with the d digits of m exactly when F(m) mod 10^d = m, where
  d = `len(str(m))`; for m = 0 that is F(0) mod 10 = 0, so 0 is printed.
- The chained comparison `…==m==print(m)` calls `print` only when the
  first equality holds, one byte under `…-m or print(m)`. The list around
  it keeps the loop going.

**Notes**

- Exact integers, a direct test of the definition.
- F(m) has about 0.21·m digits, so each step costs time proportional to m:
  the program prints about 485 terms (up to m = 648005) in 60 s. The bar
  is 370 terms (up to 210245); the b-file has 1034 terms (up to 99306245).
- The pair cannot simply be kept modulo a power of 10: the digits it throws
  away are needed once m gets one digit longer. Starting over for each
  number of digits k, with the pair taken mod 10ᵏ
  (`for m in range(k):k//10<=m==a==print(m);a,b=b,(a+b)%k` inside
  `while 1:` with `k*=10`), is 83 bytes but prints 664 terms in 3 s.
- Keeping a running power of ten instead of `10**len(str(m))` costs
  3 bytes more.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 62 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000350), CC BY-SA 4.0.
