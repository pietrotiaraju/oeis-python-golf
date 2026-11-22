# A002161

> Decimal expansion of square root of Pi.
> — [OEIS A002161](https://oeis.org/A002161)

Offset 1: 1, 7, 7, 2, 4, 5, 3, 8, 5, 0, 9, 0, 5, 5, 1, 6, 0, 2, 7, 2, 9, 8, 1, …

### Python 3 — 125 bytes

```python
import math
t=l=1;q=z=2;P=0
while-z%t<q or[print(math.isqrt(P:=P*100+z//t)%10),q:=q*100,z:=z%t*100]:l+=2;q*=l//2;z=z*l+q;t*=l
```

**How it works**

- **Square root from π.** For every real x ≥ 0, ⌊√x⌋ = isqrt(⌊x⌋), so
  ⌊√π·10ʲ⌋ = ⌊√(π·100ʲ)⌋ = isqrt(⌊π·100ʲ⌋). The program computes π in
  base 100, one certified base-100 digit at a time, keeps
  P = ⌊π·100ʲ⌋ (`P*100+` the new digit) and prints the last decimal digit
  of `math.isqrt(P)`, the (j+1)-th digit of √π = 1.77245…
- **The π spigot.** It is the halved Gibbons spigot of
  [A001672](../../A001xxx/A001672/): π = 2u,
  u = 1 + 1/3·(1 + 2/5·(1 + 3/7·(1 + …))), every tail in [1, 2]. The
  number whose digits are still to come lies in [z/t, (z+q)/t]; the
  start q = z = 2, t = 1 is π ∈ [2, 4]. Term k (l = 2k + 1) does
  q → q·k, z → z·l + q, t → t·l and halves the width at least.
- **Printing.** The two ends have the same integer part `z//t` unless
  z mod t + q > t, which `-z%t<q` tests (when z mod t = 0 it just waits
  one more term). Then that integer part is the next base-100 digit of π
  for sure (3 first, then 14, 15, 92, …); the list prints the new digit of
  √π and the interval becomes 100·(x − digit): `q*100` and `z%t*100`.
  Otherwise the body takes one more term.

**Notes**

- Exact integer arithmetic: every base-100 digit of π is certified
  (π is irrational, so none is held back forever) and the integer square
  root is exact, so the program is right for every n.
- Each printed value is one digit, so the 4300-digit int-to-str limit
  does not apply. A digit of √π needs two digits of π, about 6.6 terms of
  the series: 10000 digits take about 22 s here. The bar is 10000 of the
  20000 digits in the b-file, in 60 s.
- Keeping z unreduced saves the 15 bytes of P but is far too slow for
  this bar: it is the short-bar record below.

### Python 3, 2000 terms — 110 bytes

```python
import math
t=l=1;q=z=2
while-z%t<q or[print(math.isqrt(z//t)%10),q:=q*100,z:=z*100]:l+=2;q*=l//2;z=z*l+q;t*=l
```

**How it works**

- The same spigot and the same square-root step, but z is never reduced:
  after j printed digits the interval [z/t, (z+q)/t] encloses π·100ʲ
  itself, so when both ends have the same integer part, `z//t` is
  P = ⌊π·100ʲ⌋, and `isqrt(z//t)%10` is the (j+1)-th digit of √π.
  `q:=q*100,z:=z*100` moves on to π·100ʲ⁺¹. The test `-z%t<q` and the
  certificate are those of the main program, so it is right for every n.
- The price is speed: z//t has about 6.6·j bits, so every `z%t` is a long
  division with a long quotient, and the run time grows like the cube of
  the number of digits: 2000 digits take about 20 s here, 2800 about
  60 s. The bar of this record is 2000 digits in 60 s.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-22 | 125 | first entry |

**Python 3, 2000 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-22 | 110 | first entry: z kept unreduced, no P |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002161), CC BY-SA 4.0.
