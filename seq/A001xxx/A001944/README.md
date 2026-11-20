# A001944

> Numbers that are the sum of 4 distinct squares: of form w^2 + x^2 + y^2 + z^2 with 0 <= w < x < y < z.
> — [OEIS A001944](https://oeis.org/A001944)

Offset 1: 14, 21, 26, 29, 30, 35, 38, 39, 41, 42, 45, 46, 49, 50, 51, 53, 54, 56, …

### Python 3 — 106 bytes

```python
f=lambda n,k,j=4:any(f(n-i*i,i,j-1)for i in range(k*(n>=0<j)))or n|j==0
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
  the `any`. The default `j=4` makes `f(n,n)` ask for four squares.
- The bound k = n is enough: a square in a sum equal to n is at most n,
  so i ≤ √n < n for n ≥ 2, and 0 and 1 are not sums of four distinct
  squares.
- The main loop prints n when `f(n,n)` holds; `print` in the loop
  condition returns `None`, and `[None]` keeps the loop going.

**Notes**

- Exact integer arithmetic and an exhaustive search, so the program is
  right for every n. The search depth is 5 (four squares and the check),
  far from the recursion limit.
- The numbers that are not sums of four distinct squares are 4^k·m with m
  in the finite list [A001948](../A001948/) (Pall, 1933), so from 104 on
  every number not divisible by 4 is a term; the program does not use
  this.
- The same template with `j=5` gives [A001995](../A001995/). Writing the
  four loops out, `n in{a*a+b*b+c*c+d*d for a in range(n)if a*a<=n for b
  in range(a)…}`, is 126 bytes, and `itertools.combinations` of the
  squares up to n is 118. Three squares ([A001974](../A001974/)) and two
  ([A001983](../A001983/)) are shorter with the loops written out.
- The b-file has 1000 terms (up to 1105) and the whole of it prints in
  about 3 s here; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 106 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001944), CC BY-SA 4.0.
