# A000286

> Number of positive integers <= 2^n of form 2 x^2 + 5 y^2.
> — [OEIS A000286](https://oeis.org/A000286)

Offset 0: 0, 1, 1, 4, 5, 11, 20, 36, 65, 119, 218, 412, 770, 1466, …

### Python 3 — 80 bytes

```python
n=1
while R:=range(n):print(len({2*x*x+5*y*y-1for x in R for y in R}&{*R}));n*=2
```

**How it works**

- `n` runs through 1, 2, 4, 8, …, so a(k) is the number of distinct values
  v = 2x² + 5y² with 1 ≤ v ≤ n. Signs of x and y do not change v, so
  0 ≤ x, y is enough.
- The set holds v − 1 for every 0 ≤ x, y < n, and `&{*R}` keeps the ones in
  0 … n−1, which are exactly the v in 1 … n. The shift by one also drops
  x = y = 0 (v − 1 = −1) without a separate `-1` on the count.
- `while R:=range(n)` assigns the range in the loop condition. It stays
  nonempty because n starts at 1 and doubles after every term.
- The ranges are wide enough: v ≤ n forces x ≤ √(n/2) and y ≤ √(n/5), both
  at most n − 1 once n ≥ 2. For n = 1 the only pair is (0, 0), and the answer
  is 0 because 2x² + 5y² = 1 has no solution.
- `-1for` prints a `SyntaxWarning` to stderr, which does not count.

**Notes**

- Every pair x, y < n is tried, n² of them, and the full set is kept before
  the intersection: about 36 million distinct values at n = 2^13, about
  2.2 GB of memory. On the machine that set the bar, a(0) … a(12) print in
  about 13 s and a(13) comes at 55–60 s, right at the limit (some runs
  miss it). The bar is 12 terms in 60 s.
- Keeping only values ≤ n inside the set keeps the memory to n values and
  reaches a(13) in about 30 s, but costs bytes:
  `{v for x in R for y in R if(v:=2*x*x+5*y*y)<=n}` with `-1` on the count
  is 90 bytes, and clipping with `{min(n+1,2*x*x+5*y*y)for…}` and `-2` on
  the count (R = range(n+1)) is 87.
- Trying only x, y < 2^(⌊k/2⌋+1), which is enough for the bound 2^k, makes
  each term linear in 2^k: `i=0` +
  `while 1:R=range(2<<i//2);print(len({2*x*x+5*y*y-1for x in R for y in R}&{*range(2**i)}));i+=1`
  (97 bytes) prints a(23) after about 28 s.
- Walrus in the condition, `while[print(len({*(R:=range(n))}&{…}))]:n*=2`,
  is 81 bytes.
- The b-file has 49 terms (n = 0 to 48); the program is exact for every n,
  and only time and memory stop it.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 81 | first entry |
| 2026-11-06 | Python 3 | 80 | assign `R` in the loop condition |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000286), CC BY-SA 4.0.
