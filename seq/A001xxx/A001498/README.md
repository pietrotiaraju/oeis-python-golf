# A001498

> Triangle a(n,k) (n >= 0, 0 <= k <= n) of coefficients of Bessel polynomials y_n(x) (exponents in increasing order).
> — [OEIS A001498](https://oeis.org/A001498)

Offset 0: 1, 1, 1, 1, 3, 3, 1, 6, 15, 15, 1, 10, 45, 105, 105, 1, 15, 105, 420, 945, …

### Python 3 — 76 bytes

```python
m=0
while[t:=1,m:=m+1]:
 for k in range(m):print(t);t=t*(m+k)*(m+~k)//2//-~k
```

**How it works**

- a(n,k) = (n+k)!/(2^k·k!·(n−k)!), the coefficient of x^k in the Bessel
  polynomial y_n(x). Along a row,
  **a(n,k+1) = a(n,k)·(n+k+1)(n−k)/(2(k+1))**, starting from a(n,0) = 1.
- `m` = n+1 is the row length: the header `while[t:=1,m:=m+1]:` resets
  `t` to a(n,0) and moves to the next row (a non-empty list is always
  true). The inner loop prints `t` and steps it with
  `t*(m+k)*(m+~k)//2//-~k` = t·(n+k+1)(n−k)/2/(k+1).
- Both floor divisions are exact: the product is 2(k+1)·a(n,k+1), and
  after `//2` it is (k+1)·a(n,k+1). After the last entry (k = n) the
  factor n−k = 0 leaves t = 0, which is never printed.

**Notes**

- The closed form `comb(n+k,k)*perm(n,k)>>k` in the usual triangle walk
  (as in [A001497](../A001497/)) is 79 bytes, and the ratio inside that
  walk, `t=k and t*(n+k)*(n-k+1)//2//k or 1`, is 77.
- Exact integer arithmetic, so the program is right for every n; the
  first entry over the 4300-digit int-to-str limit is a(1424, 1421), the
  term with index 1016021 (counting from 0).
- The b-file has 1326 terms (rows 0 to 50); all of them print in well
  under a second, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 76 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001498), CC BY-SA 4.0.
