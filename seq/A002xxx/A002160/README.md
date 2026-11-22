# A002160

> Nearest integer to Pi^n.
> — [OEIS A002160](https://oeis.org/A002160)

Offset 0: 1, 3, 10, 31, 97, 306, 961, 3020, 9489, 29809, 93648, 294204, …

### Python 3 — 106 bytes

```python
t=l=1;q=z=2;n=0
while 2*z**n//t**n<(a:=2*(z+q)**n//t**n)or[print(a+1>>1),n:=n+1]:l+=2;q*=l//2;z=z*l+q;t*=l
```

**How it works**

- **A shrinking interval around π.** This is the loop of ⌊πⁿ⌋ in
  [A001672](../../A001xxx/A001672/): the halved Gibbons spigot
  π = 2u, u = 1 + 1/3·(1 + 2/5·(1 + 3/7·(1 + …))). After k terms π lies
  strictly inside [z/t, (z+q)/t] (every tail of the series lies in
  [1, 2]); the start q = z = 2, t = 1 is π ∈ [2, 4]. Taking term k
  (l = 2k + 1) does q → q·k, z → z·l + q, t → t·l, which multiplies the
  width q/t by k/(2k+1) < ½.
- **Rounding through ⌊2x⌋.** The nearest integer to x is ⌊x + ½⌋, and
  ⌊x + ½⌋ = ⌊(⌊2x⌋ + 1)/2⌋ (nested floors), so it is enough to know
  m = ⌊2πⁿ⌋; then a(n) = (m + 1) >> 1, the `a+1>>1` in the code.
  Powers keep the order, so `2*z**n//t**n` ≤ m ≤ `2*(z+q)**n//t**n`; when
  both ends agree they equal m, the list prints a(n) and steps n.
  Otherwise the body takes in one more term and the same n is tried
  again.
- **No ties, no stalls.** For n ≥ 1, πⁿ is irrational (π is
  transcendental), so 2πⁿ is never an integer: πⁿ is never exactly
  halfway between two integers, the rounding is well defined, and once
  the interval is narrow enough both ends of 2·[z/t, (z+q)/t]ⁿ fall
  between the same two integers. For n = 0 both ends give 2 at once and
  the program prints 1.

**Notes**

- Exact integer arithmetic throughout, so every term is certified and the
  program is right for every n.
- The b-file has 29 terms (a(0) to a(28)); they all come in well under a
  second. The bar is the whole b-file, in 60 s.
- Rounding each end directly, `(2*z**n+t**n)//(2*t**n)`, is longer, and so
  is computing tⁿ once with `(T:=t**n)`. The original form of the spigot
  (π in [(y−q)/t, y/t], as in [A000796](../../A000xxx/A000796/)) costs two
  bytes more in the update.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 106 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002160), CC BY-SA 4.0.
