# A001261

> Number of permutations of length n with 5 consecutive ascending pairs.
> — [OEIS A001261](https://oeis.org/A001261)

Offset 1: 0, 0, 0, 0, 0, 1, 6, 63, 616, 6678, 77868, 978978, 13216104, 190899423, 2939850914, …

### Python 3 — 56 bytes

```python
e=m=-2
while[print(e*~-m*-~m*(m+2)//120)]:m+=1;e=(e^1)*m
```

**How it works**

- A permutation of [n] with exactly k successions (i directly followed
  by i + 1) is built from one with none: glue each succession into a
  block. That gives C(n−1, k)·S(n−k), where S(j) counts the permutations
  of [j] without successions, and S(j) = D(j+1)/j with D the derangement
  numbers ([A000255](../../A000xxx/A000255/), as on
  [A001260](../A001260/)). For k = 5,
  a(n) = C(n−1, 5)·D(n−4)/(n−5) = (n−1)(n−2)(n−3)(n−4)·D(n−4)/120,
  which also holds (as 0) for n ≤ 5.
- `e` is m·D(m−1) with m = n − 3, updated by `e=(e^1)*m` as in
  [A000313](../../A000xxx/A000313/): D(j) = j·D(j−1) + (−1)ʲ, and
  j·D(j−1) is even exactly when j is even, so `^1` adds the ±1. The
  remaining factors are (m − 1)(m + 1)(m + 2), written `~-m*-~m*(m+2)`.
- `e=m=-2` gives n = 1. The factors m + 2 and m − 1 vanish at m = −2 and
  m = −1, which hides the junk values of `e`; m = 0 resets `e` to 0, and
  from there on `e` = m·D(m−1) exactly.

**Notes**

- Tracking D(m) itself with `d=d*m^1` (since m·D(m−1) is odd exactly
  when m is) is 2 bytes shorter in the update but leaves four factors
  m(m+1)(m+2)(m+3) to print: 58 bytes. `(m*m-1)*(m+2)` for the product
  ties at 56.
- Exact integer arithmetic; checked against a count of all permutations
  for n ≤ 9.
- The b-file has 200 terms; the bar is all of them in 60 s, which print
  at once. a(1559) is the first term with more than 4300 digits (Python's
  int-to-str limit), so the program stops with a `ValueError` after
  a(1558).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001261), CC BY-SA 4.0.
