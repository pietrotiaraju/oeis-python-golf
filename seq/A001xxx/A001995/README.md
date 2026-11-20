# A001995

> Numbers that are the sum of 5 distinct squares: of form v^2 + w^2 + x^2 + y^2 + z^2 with 0 <= v < w < x < y < z.
> — [OEIS A001995](https://oeis.org/A001995)

Offset 1: 30, 39, 46, 50, 51, 54, 55, 57, 62, 63, 65, 66, 70, 71, 74, 75, 78, 79, …

### Python 3 — 106 bytes

```python
f=lambda n,k,j=5:any(f(n-i*i,i,j-1)for i in range(k*(n>=0<j)))or n|j==0
n=0
while[f(n,n)and print(n)]:n+=1
```

**How it works**

- `f(n,k,j)` tells whether n is a sum of j distinct squares i² with
  0 ≤ i < k. Take the largest square i² of such a sum: the other j − 1 are
  distinct squares of numbers below i. So f(n, k, j) is true when
  f(n − i², i, j − 1) is true for some i < k, and with no squares left
  (j = 0) it is true only for n = 0. Passing i as the new bound keeps the
  squares distinct and lists each set once, largest first.
- `range(k*(n>=0<j))` is empty once the remainder n is negative or no
  squares are left, so `any` is false there and `n|j==0` decides: it holds
  only for n = j = 0. While n ≥ 0 and j > 0 it is false, so the result is
  the `any`. The default `j=5` makes `f(n,n)` ask for five squares.
- The bound k = n is enough: a square in a sum equal to n is at most n,
  so i ≤ √n < n for n ≥ 2, and 0 and 1 are not sums of five distinct
  squares.
- The main loop prints n when `f(n,n)` holds; `print` in the loop
  condition returns `None`, and `[None]` keeps the loop going.

**Notes**

- Exact integer arithmetic and an exhaustive search, so the program is
  right for every n. The search depth is 6, far from the recursion limit.
- Same template as the four squares of [A001944](../A001944/), with
  `j=5`. Five nested loops written out are much longer.
- The last number below 1076 that is not a term is 224: every number
  from 225 to the end of the b-file is a sum of five distinct squares.
  The program does not rely on this and tests every n.
- The b-file has 1000 terms (up to 1076) and the whole of it prints in
  about 5 s here; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 106 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001995), CC BY-SA 4.0.
