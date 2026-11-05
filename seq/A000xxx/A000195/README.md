# A000195

> a(n) = floor(log(n)).
> — [OEIS A000195](https://oeis.org/A000195)

Offset 1: 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, …

### Python 3 — 63 bytes

```python
from decimal import*
n=1
while[print(Context(n).ln(n)//1)]:n+=1
```

**How it works**

- `Context(n)` is a decimal context with n significant digits (the
  precision is its first argument), and its `ln` method takes the int n
  directly, so `Context(n).ln(n)` is ln n to n digits, 9 bytes under
  `Decimal(n).ln(Context(n))`. `//1` floors it exactly (in the default
  28-digit context, plenty for an integer part).
- Python documents `ln` as correctly rounded. Rounding is monotone and
  k = ⌊ln n⌋ and k + 1 have far fewer than n digits, so the result r lies
  in [k, k + 1], and `r//1` is k unless r rounded up to b = k + 1.
- That needs b − ln n below one unit of the n-th digit, at most
  10^(d−n) with d the number of digits of b. Since b − ln n ≥ 1 − n/e^b,
  the distance from e^b to the nearest integer would have to be below
  e^b·10^(d−n), with n > e^(b−1).
- Hermite's integral rules that out. With f = x^m(1−x)^m/m! and m = b²,
  J = b^(2m+1)∫₀¹ e^(bx) f(x) dx equals Qe^b − P for integers
  P, Q (the derivatives of f at 0 and 1 are integers), with
  2^(−b²)/(4b) ≤ J < 1/2 for b ≥ 4 and |Q| ≤ (3b²)^(b²). For any
  integer a, Q(e^b − a) is J minus an integer, so its size is at least J,
  and |e^b − a| ≥ (6b²)^(−b²)/(4b).
- In logs that is b² ln 6b² + ln 4b against (e^(b−1) − d) ln 10 − b
  needed: 384 against 2515 at b = 8, and the right side grows like e^b.
  So every n beyond e^7 ≈ 1097 is safe, and the n below it are in the bar.

**Notes**

- n digits is far more precision than the proof needs (a few hundred would
  do for n near 10⁴), but `Context(n)` is the shortest precision that
  grows. ln to n digits gets slow: about 1000 terms in 10 s and 1500 in
  60 s here. The bar is 1200 terms in 60 s.
- Floats are not enough: `math.log` returns exactly 33.0 at
  n = ⌊e³³⌋ = 214643579785916, where a(n) = 32.
- An all-integer program (⌊e^a⌋ from the series as in
  [A000149](../A000149/), compared with n) came to 90 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 63 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000195), CC BY-SA 4.0.
