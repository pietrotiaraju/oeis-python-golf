# A000227

> Nearest integer to e^n.
> — [OEIS A000227](https://oeis.org/A000227)

Offset 0: 1, 3, 7, 20, 55, 148, 403, 1097, 2981, 8103, …

### Python 3 — 71 bytes

```python
from decimal import*
n=0
while[print(round(Context(1<<n).exp(n)))]:n+=1
```

**How it works**

- `Context(1<<n)` is a decimal context with 2^n significant digits, and its
  `exp` method takes the int n directly, so `Context(1<<n).exp(n)` is e^n to
  2^n digits. `round` turns a Decimal into the nearest int (ties to even)
  exactly, whatever its size.
- Python documents `exp` as correctly rounded, so with p = 2^n and
  10^E ≤ e^n < 10^(E+1) the result x satisfies |x − e^n| ≤ ½·10^(E+1−p).
  `round(x)` can only miss the nearest integer to e^n if a half-integer h
  lies between x and e^n (x = h included), and then |2e^n − a| ≤
  10^(E+1−p) for the odd integer a = 2h.
- Hermite's integral rules that out for n = b ≥ 8. With
  f = x^m(1−x)^m/m! and m = b², J = b^(2m+1)∫₀¹ e^(bx) f(x) dx equals
  Qe^b − P for integers P, Q (the derivatives of f at 0 and 1 are
  integers). Since e^(bx) ≥ 1 and m! ≤ m^m,
  J ≥ b^(2m+1)·m!/(2m+1)! ≥ 4^(−b²)/(3b); since f ≤ 4^(−m)/m!,
  J < b·e^b·(b²/4)^m/m! < 1/4 for b ≥ 3; and
  |Q| ≤ (b + 2m)^m ≤ (3b²)^(b²).
- For any integer a, Q(2e^b − a) = 2J − (aQ − 2P) is 2J minus an integer,
  with 0 < 2J < ½, so its size is at least 2J and
  |2e^b − a| ≥ 2J/|Q| ≥ 2/(3b·(12b²)^(b²)).
- In powers of ten that is above 10^(E+1−p) as soon as
  2^b > b²·log₁₀(12b²) + b·log₁₀ e + 1 + log₁₀(3b/2): 256 against 191 at
  b = 8, and from there the left side doubles at each step while the right
  side grows by less than 40 %. So every n ≥ 8 is safe, and the n below it
  are in the bar (n = 0 is exact: exp(0) = 1).

**Notes**

- 2^n is the shortest precision that is never 0 (`Context(0)` is a
  `ValueError`) and outgrows the b²·log b digits the proof needs.
  `n**3+1` also works and is faster (27 terms in 60 s here), for 2 more
  bytes. A precision of `n*n+1` digits (72 bytes) would be fast, but the
  Hermite bound needs more than n² digits, and no known lower bound for
  |2e^n − a| covers it.
- `exp` gets slow at thousands of digits: about 10 s at 16384 digits and
  40 s at 32768 here, so n = 0..15 (16 terms) take about 56 s. The bar is
  15 terms in 60 s.
- An exact all-integer program in the style of [A000149](../A000149/) is
  83 bytes. It sums the series for 2e^n − 1 over a common denominator
  (M/F with M = F = 1 at the start, adding 2n^d each step) and stops when
  the gap to the next integer certifies the floor, as there; then
  ⌊2e^n − 1⌋ + 2 >> 1 is the nearest integer. It prints the whole b-file
  at once (527 terms in 10 s):

  ```python
  n=0
  while 1:
   M=F=d=1
   while-M%F<n**d:M=M*d+2*n**d;F*=d;d+=1
   print(M//F+2>>1);n+=1
  ```

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000227), CC BY-SA 4.0.
