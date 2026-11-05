# A000076

> Number of integers <= 2^n of form 4 x^2 + 4 x y + 5 y^2.
> — [OEIS A000076](https://oeis.org/A000076)

Offset 0: 0, 0, 1, 2, 4, 7, 14, 24, 43, 82, 149, 284, 534, 1015, 1937, …

Only positive integers count: 0 = 4·0² + 4·0·0 + 5·0² would make a(0) = 1,
but a(0) = 0.

### Python 3 — 97 bytes

```python
n=0
while r:=range(2<<n//2):print(len({min(4*x*(x-y)+5*y*y,2**n+1)for x in r for y in r})-2);n+=1
```

**How it works**

- Turning y into −y gives the same set of values, so the program uses
  4x² − 4xy + 5y², written `4*x*(x-y)+5*y*y`. That equals (2x − y)² + 4y².
- With x, y ≥ 0 that form still reaches every value. A value of the form is
  a² + 4b² with a = 2X + Y and b = Y for some integers X, Y, so a ≡ b
  (mod 2); signs do not matter, so take a, b ≥ 0. Then y = b and
  x = (a + b)/2 are whole and ≥ 0, and 2x − y = a.
- For a value up to 2ⁿ, a + b ≤ (√5/2)·2^(n/2) by Cauchy–Schwarz, so
  x ≤ 0.56·2^(n/2) and y ≤ 0.5·2^(n/2). `range(2<<n//2)` reaches
  2^(⌊n/2⌋+1), past both bounds for every n, so one range serves both
  variables.
- `min(…,2**n+1)` folds every value above 2ⁿ into the single value 2ⁿ + 1.
  The cap is always in the set: the largest y with x = 0 gives
  5y² > 2ⁿ. The set then holds 0, the cap, and each positive value ≤ 2ⁿ
  once, so `-2` leaves a(n).
- The cap has to be 2ⁿ + 1. Capping at 2ⁿ and subtracting 1, as in
  [A000050](../A000050/), would be wrong for n = 0, 1 and 3: 1, 2 and 8
  are not values of the form.
- `while r:=range(2<<n//2):` names the range and keeps the loop going (a
  non-empty range is truthy), with the print and `n+=1` after the colon.
  The program has the same shape as [A000018](../A000018/), whose form
  x² + 16y² has the same discriminant, −64.

**Notes**

- `(2*x-y)**2+4*y*y` is 1 byte longer. The original
  `4*x*x+4*x*y+5*y*y` needs negative values in the range. `x*x+4*y*y` with
  y in `r[x%2::2]`, which keeps a ≡ b (mod 2) by stepping, is 2 bytes
  longer in all.
- Term n runs through 4^(⌊n/2⌋+1) pairs, so the program prints
  a(0)…a(23) in about 17 s and a(24) at about 43 s (CPython 3.14). The bar
  is 24 terms in 60 s, the same as for A000018; the b-file goes to n = 39,
  far beyond any enumeration.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 97 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000076), CC BY-SA 4.0.
