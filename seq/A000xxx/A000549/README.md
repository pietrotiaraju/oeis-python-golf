# A000549

> Numbers that are the sum of 2 squares but not sum of 3 nonzero squares.
> — [OEIS A000549](https://oeis.org/A000549)

Offset 1: 1, 2, 4, 5, 8, 10, 13, 16, 20, 25, …

### Python 3 — 99 bytes

```python
S={n:=1}
while[{n-a-b for a in S for b in S}&S or S&{n-a for a in S|{0}}and print(n)]:n+=1;S|={n*n}
```

**How it works**

- When n is tested, `S` holds the positive squares 1, 4, …, n², so it contains
  every positive square up to n.
- `{n-a-b for a in S for b in S}&S` is non-empty exactly when n = a + b + c
  with a, b, c positive squares: c = n − a − b must itself lie in S.
- `S&{n-a for a in S|{0}}` is non-empty exactly when n = a + c with c a
  positive square and a a square, 0 allowed: that is, n is a sum of two
  squares (one of them is positive since n ≥ 1).
- `Y or X and print(n)` prints n when Y is empty and X is not; both sets are
  falsy when empty. The list around it keeps the loop condition true.
- The body moves to n + 1 and adds (n + 1)² to `S`. Larger squares in `S` are
  harmless: they only give negative differences.

**Notes**

- Other versions: the same tests with `any(n-a-b in S for a in S for b in S)`
  instead of the set of differences are 104 bytes and about five times
  faster (it stops at the first representation); a list of squares with
  chained comparisons `0<a<=b<=n-a-b in s` is 111; the `isqrt` square tests
  were 173.
- The program checks the definition directly, so it is right for every n.
  It does not use the pattern seen in the data (every b-file term is 4^k·m
  with m ∈ {1, 2, 5, 10, 13, 25, 37, 58, 85, 130}), which the OEIS entry only
  states as an observation and an empirical generating function.
- Each n builds a set of about n² differences: 33 terms (up to 640) in 60 s
  here, the bar after about 14 s. The b-file has 113 terms (up to 41943040);
  the bar is 30 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 186 | first entry |
| 2026-11-06 | Python 3 | 173 | reuse exact residuals in the two square tests |
| 2026-11-07 | Python 3 | 99 | sets of squares and of differences instead of isqrt tests |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000549), CC BY-SA 4.0.
