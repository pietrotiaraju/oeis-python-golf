# A001345

> a(n) = Sum_{k = 0..3} (n+k)! C(3,k).
> — [OEIS A001345](https://oeis.org/A001345)

Offset -1: 7, 16, 49, 212, 1158, 7584, 57720, 499680, 4843440, 51932160, …

For n ≥ 0, a(n) = n! + 3·(n+1)! + 3·(n+2)! + (n+3)!. At n = −1 the k = 0
term would be (−1)!, so the sum does not define a(−1); the OEIS gives
a(−1) = 7 (Marcus's PARI program on the entry).

### Python 3 — 54 bytes

```python
f=7;n=0
while[print(f*n*~-(n+3)**2+f)]:f=f*n or 1;n+=1
```

**How it works**

- The loop counter `n` is j = n + 1 (it starts at 0 for a(−1)). Dividing
  each (j−1+k)! by (j−1)! leaves a rising product, so for j ≥ 1
  a(j−1) = (j−1)!·(1 + 3j + 3j(j+1) + j(j+1)(j+2))
  = (j−1)!·(j³ + 6j² + 8j + 1) = (j−1)! + j!·((j+3)² − 1).
- `~-x` is x − 1 and `**` binds tighter than the unary operators, so
  `~-(n+3)**2` is (j+3)² − 1; with `f` = (j−1)! the print is
  `f*n*~-(n+3)**2+f`.
- `f` starts at 7, so at j = 0 the print gives 7 = a(−1). Then
  `f=f*n or 1` turns 7·0 = 0 into 1 = 0!; from j = 1 on f·j is never 0, so
  f = (j−1)! at every later print.
- The value 7 is the only stored term. It is what the sum gives if (−1)! is
  read as −1 (−1 + 3·0! + 3·1! + 2! = 7), as in
  [A001344](../A001344/), [A001346](../A001346/) and
  [A001347](../A001347/); it is also a(−1) + a(0) = 2 + 5 of A001344, the
  Pascal step C(3, k) = C(2, k) + C(2, k−1) that links the two sums for
  n ≥ 0.
- `print` returns `None` and `[None]` is truthy, so the loop never ends.
  Exact integers, so every term is right.

**Notes**

- `j*(j+2)*(j+4)` as `n*(n+2)*(n+4)` is a byte longer than
  `n*~-(n+3)**2`; printing a(−1) separately (`f=n=1;print(7)` and `f*=n`)
  is 55 bytes, and so is computing it from (−1)! = −1 as in
  [A001346](../A001346/) (`g=1;x=3` /
  `while[print(g*~-x**2+g//(x-3or-1))]:x+=1;g*=x-3`).
- Python's 4300-digit int-to-str limit stops the program at a(1556), the
  first term with more than 4300 digits, after printing a(−1) to a(1555).
- The b-file has 102 terms (n = −1 to 100); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001345), CC BY-SA 4.0.
