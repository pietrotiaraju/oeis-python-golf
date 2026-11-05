# A000047

> Number of integers <= 2^n of form x^2 - 2y^2.
> — [OEIS A000047](https://oeis.org/A000047)

Offset 0: 1, 2, 3, 5, 8, 15, 26, 48, 87, 161, 299, 563, 1066, 2030, 3885, 7464, …

### Python 3 — 95 bytes

```python
n=0
while r:=range(2<<n//2):print(len({v for x in r for y in r if~-(v:=2*y*y-x*x)>>n==0}));n+=1
```

**How it works**

The terms count the positive integers m ≤ 2ⁿ that can be written as
x² − 2y² (a(0) = 1 counts only m = 1). The program collects the distinct
values in that range and counts them.

- It uses 2y² − x² instead of x² − 2y², which gives the same positive
  values: multiplying x + y√2 by the unit 1 + √2 flips the sign of
  x² − 2y². The flipped form needs a smaller search box.
- Every m > 0 of the form 2y² − x² has a solution with 0 ≤ x, y ≤ √m.
  Take a solution with x, y ≥ 0 and y as small as possible. If y > √m,
  then x² = 2y² − m lies between y² and 2y², so y < x < √2·y. Multiplying
  by the unit 3 − 2√2 gives the solution (|3x − 4y|, 3y − 2x), and
  0 < 3y − 2x < y contradicts the choice of y.
- So for m ≤ 2ⁿ, x and y never pass ⌊2^(n/2)⌋, and `range(2<<n//2)`
  (up to 2^(n//2+1) − 1) covers that for every n. The same box for
  x² − 2y² would need x up to 2^((n+1)/2), which `3<<n//2` covers at
  the same length but with more than twice the pairs.
- `~-v>>n==0` is (v − 1) >> n == 0, which holds exactly when
  0 ≤ v − 1 < 2ⁿ, that is 0 < v ≤ 2ⁿ: one test for both ends. It is a
  byte shorter than `0<v<=2**n`.
- A range is truthy when it is not empty, so `while r:=range(…):` names
  the box and keeps the loop going. That is 1 byte shorter than
  `while 1:r=range(…);` and 5 bytes shorter than the
  `while[print(len([r:=…]and{…}))]:n+=1` layout of
  [A000018](../A000018/).

**Notes**

- Term n costs at most 2ⁿ⁺² pairs and the set grows to a(n) elements, so
  the program prints a(0)…a(24) in about 20 s and a(25) at about 34 s. The
  bar is 25 terms in 60 s; the b-file goes to n = 50, far beyond any
  enumeration.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 95 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000047), CC BY-SA 4.0.
