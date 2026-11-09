# A001263

> Triangle of Narayana numbers T(n,k) = C(n-1,k-1)*C(n,k-1)/k with 1 <= k <= n, read by rows. Also called the Catalan triangle.
> — [OEIS A001263](https://oeis.org/A001263)

Offset 1: 1, 1, 1, 1, 3, 1, 1, 6, 6, 1, 1, 10, 20, 10, 1, 1, 15, 50, 50, 15, 1, …

Row n holds T(n, 1), …, T(n, n); T(n, k) counts the Dyck paths of
semilength n with k peaks, and row n sums to the Catalan number C(n).

### Python 3 — 68 bytes

```python
n=k=t=1
while[print(t)]:t=t*(k-n)*(k+~n)//k//-~k or 1;k=k%n+1;n+=k<2
```

**How it works**

- Along a row the ratio of neighbours is
  T(n, k+1)/T(n, k) = [C(n−1, k)/C(n−1, k−1)]·[C(n, k)/C(n, k−1)]·k/(k+1)
  = ((n−k)/k)·((n−k+1)/k)·(k/(k+1)) = (n−k)(n−k+1)/(k(k+1)).
  `(k-n)*(k+~n)` is (k−n)(k−n−1) = (n−k)(n−k+1), and `//k//-~k` divides
  by k and then by k + 1.
- The division is exact: t·(n−k)(n−k+1) = k(k+1)·T(n, k+1), and for a
  non-negative A, ⌊⌊A/k⌋/(k+1)⌋ = ⌊A/(k(k+1))⌋.
- After the last entry of a row (k = n) the factor n − k is 0, so `t`
  becomes 0 and `or 1` turns it into 1 = T(n+1, 1), the first entry of the
  next row.
- `k=k%n+1` steps k through 1, …, n and then back to 1; `n+=k<2` moves to
  the next row exactly when k wraps. Row 1 (n = k = 1) wraps at once.
- `print` returns `None` and `[None]` is a non-empty list, so the loop
  never ends. Exact integers throughout, so every entry is right.

**Notes**

- With `from math import*`, `comb(n,k)*comb(n,k-1)//n` in the same loop
  is 77 bytes (T(n, k) = C(n, k)·C(n, k−1)/n). Dividing by `(k*k+k)or 1`
  instead of `k//-~k or 1` is the same length; `(n-k)*(n-k+1)` is 1 byte
  longer than `(k-n)*(k+~n)`.
- The entries reach 4301 digits only around row n ≈ 7100 (the middle of
  row n is about 4ⁿ/n²), some 25 million terms in, so Python's 4300-digit
  int-to-str limit is far beyond reach.
- The b-file has 5050 terms (rows 1 to 100); the bar is the whole b-file
  in 60 s, which takes about 0.1 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001263), CC BY-SA 4.0.
