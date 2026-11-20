# A001974

> Numbers that are the sum of 3 distinct squares, i.e., numbers of the form x^2 + y^2 + z^2 with 0 <= x < y < z.
> — [OEIS A001974](https://oeis.org/A001974)

Offset 1: 5, 10, 13, 14, 17, 20, 21, 25, 26, 29, 30, 34, 35, 37, 38, 40, 41, 42, …

### Python 3 — 105 bytes

```python
n=0
while[n in{a*a+b*b+c*c for a in range(n)if a*a<=n for b in range(a)for c in range(b)}==print(n)]:n+=1
```

**How it works**

- For each n the set comprehension lists every a² + b² + c² with
  0 ≤ c < b < a and a² ≤ n, and n is printed when it is in that set.
  Each sum with x < y < z of the definition appears as (c, b, a) =
  (x, y, z), and z² ≤ n, so nothing is missed.
- `range(n)` with the filter `if a*a<=n` keeps a ≤ √n; for n ≥ 2 that is
  below n, and 0 and 1 are not sums of three distinct squares. The filter
  sits on the outer loop, so each n costs about n + n^(3/2)/6 steps instead
  of n³/6.
- `n in S==print(n)` is a chained comparison: `print` runs only when
  `n in S` holds, and the list `[False]` keeps the loop going either way.

**Notes**

- Exact integer arithmetic and an exhaustive search, so the program is
  right for every n.
- The recursive search of [A001944](../A001944/) with `j=3` is 106 bytes,
  one more. By Halter-Koch (1982), the sums of three squares that are not
  sums of three distinct squares are 4^j·s for 23 known values of s and
  possibly one unknown s > 5·10^10 (see the OEIS page), so a closed test
  is out of reach; the search needs no such result.
- The b-file has 1000 terms (up to 1284) and the whole of it prints in
  about a second; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 105 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001974), CC BY-SA 4.0.
