# A000046

> Number of primitive n-bead necklaces (turning over is allowed) where
> complements are equivalent.
> — [OEIS A000046](https://oeis.org/A000046)

Offset 0: 1, 1, 1, 1, 2, 3, 5, 8, 14, 21, 39, 62, 112, 189, 352, 607, …

### Python 3 — 133 bytes

```python
import math
n=1;a=[4]
while[print(a[-1]>>2)]:a+=sum((2-n//(g:=math.gcd(j,n))%2<<g)+(2<<n//2)-(g==j)*n*a[j]for j in range(n))//n,;n+=1
```

**How it works**

- Every necklace counted by [A000011](../A000011/) (same symmetries, not
  necessarily primitive) is a primitive one of some length d | n repeated
  n/d times, so A000011(n) = Σ a(d) over the divisors d of n, as on the
  OEIS page. That gives a(n) = A000011(n) − Σ a(d) over the divisors d < n,
  with no Möbius function needed.
- The list `a` holds b(k) = 4·a(k). For each rotation j,
  `(2-n//g%2<<g)+(2<<n//2)` is the Burnside term from the A000011 page, and
  the terms add up to 4n·A000011(n).
- `-(g==j)*n*a[j]` subtracts n·b(d) = 4n·a(d) for each proper divisor d.
  For 1 ≤ j < n, gcd(j, n) = j exactly when j divides n, and for j = 0 the
  gcd is n, not 0, so the loop over rotations also walks the divisors
  d < n. For n = 6 that is j = 1, 2, 3, while j = 4 has gcd 2.
- The sum is then 4n·a(n), and `//n` leaves b(n), appended as a one-tuple.
  Keeping 4·a in the list saves the `//4` and the `*4` on each subtracted
  term, for a `>>2` in the print: storing a(n) itself is 134 bytes.
- `a=[4]` is b(0), so the first line is a(0) = 1. j = 0 never passes the
  `g==j` test, so b(0) is never subtracted. The loop condition
  `[print(…)]` is a non-empty list, so always true.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(n) is
  about 2ⁿ/(4n), which passes the 4300-digit int-to-str limit near
  n = 14 300.
- Each term costs n gcds: the whole b-file (1001 terms, up to n = 1000)
  prints in about 0.5 s. The bar is the whole b-file in 60 s.
- Summing the divisors separately, with
  `-sum(a[d]for d in range(1,n)if n%d<1)`, is 156 bytes. Halving
  everything, with `(1<<g>>n//g%2)+(1<<n//2)`, `a=[2]` and `>>1`, is 134.
  `while n:=len(a):` in place of `n=1;` … `;n+=1` ties at 133.

### Python 3 + sympy — 119 bytes

```python
from sympy import*
n=1;k=0
while[print(sum(mobius(d)*((d%2<<n//d)+(n<<n//d//2+1))for d in divisors(n))//4//n)]:n+=k;k=1
```

- Robert A. Russell's formula on the OEIS page,
  a(n) = (Σ_{odd d|n} μ(d)·2^(n/d) / (2n) + Σ_{d|n} μ(n/d)·2^⌊d/2⌋) / 2,
  times 4n and with d → n/d in the second sum, is
  4n·a(n) = Σ_{d|n} μ(d)·((d mod 2)·2^(n/d) + n·2^(⌊n/d/2⌋+1)).
  `d%2<<n//d` keeps only the odd d in the first part, and `mobius` and
  `divisors` come from the star import.
- n = 0 would divide by zero, but a(0) = a(1) = 1, so the loop prints
  n = 1 twice: `k` is 0 on the first pass, then 1 (as in A000011).
- Multiplying by 2n instead, `(d%2<<n//d-1)+(n<<n//d//2)` with `//2//n`,
  ties at 119.
- The whole b-file prints in about 2 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 133 | first entry |
| 2026-11-05 | Python 3 + sympy | 119 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000046), CC BY-SA 4.0.
