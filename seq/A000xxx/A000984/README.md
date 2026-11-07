# A000984

> Central binomial coefficients: binomial(2*n,n) = (2*n)!/(n!)^2.
> — [OEIS A000984](https://oeis.org/A000984)

Offset 0: 1, 2, 6, 20, 70, 252, 924, 3432, 12870, 48620, 184756, 705432, …

### Python 3 — 39 bytes

```python
c=n=1
while[print(c)]:c=4*c-2*c//n;n+=1
```

**How it works**

- C(2n, n) = C(2n−2, n−1)·(4n−2)/n = 4·C(2n−2, n−1) − 2·C(2n−2, n−1)/n.
  The second part is an integer (it is 4c − C(2n, n); in fact C(2n−2, n−1)/n
  is the Catalan number Cₙ₋₁), so `c=4*c-2*c//n` is exact and 2 bytes under
  `c=c*(4*n-2)//n`.
- c and the counter n start together at 1 (`c=n=1`): the first print is
  C(0, 0) = 1 and the pass with n computes C(2n, n).

**Notes**

- Other versions: `math.comb(2*n,n)` in a counting loop is 51 bytes. The
  Catalan numbers [A000108](../A000108/) use the same loop with
  `c=4*c-6*c//n`.
- Exact integer arithmetic.
- The b-file has 1501 terms (up to a(1500)); they print at once. The bar
  is the whole b-file in 60 s. a(7146) is the first term with more than
  4300 digits, so printing stops there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000984), CC BY-SA 4.0.
