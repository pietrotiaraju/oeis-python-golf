# A000419

> Numbers that are the sum of 3 but no fewer nonzero squares.
> — [OEIS A000419](https://oeis.org/A000419)

Offset 1: 3, 6, 11, 12, 14, 19, 21, 22, 24, 27, …

### Python 3 — 110 bytes

```python
s=[];t={n:=0}
while 1:
 if n==len(s)**2:s+=n,;t|={n+x for x in s}
 if{n-x for x in s}&t^{n}>{n}:print(n)
 n+=1
```

**How it works**

- n is a sum of three nonzero squares and of no fewer exactly when n is a sum
  of three squares (zeros allowed) but not of two: if n = x² + y² + z² and n
  is not a sum of two squares, none of x, y, z is 0. The program scans
  n = 0, 1, 2, … with s, the list of squares 0, 1, 4, … up to n, and t, the
  set of all sums of two entries of s.
- s holds 0², …, (len(s) − 1)², so `len(s)**2` is the next square. When n
  reaches it, n is appended first and `t|={n+x for x in s}` adds n plus every
  square so far, n + n included. So at the test t contains every x² + y² with
  x², y² ≤ n, which covers all two-square representations of n.
- `{n-x for x in s}&t` is the set A of the numbers n − x² (x² ≤ n) that are
  sums of two squares. A is nonempty iff n is a sum of three squares, and
  since 0 is in s, n ∈ A iff n itself is a sum of two squares.
- `A^{n}>{n}` is true iff A is nonempty and n ∉ A: if n ∈ A the symmetric
  difference drops n and is no superset of {n}; if A is empty it is {n}
  itself, not a proper superset.
- `t={n:=0}` sets n inside the set display.

**Notes**

- The test `{n}-t and{n-x for x in s}&t`: 111 bytes. A root counter
  (`if n==k*k:…;k+=1`) instead of `len(s)**2`: 112. `while n:=n+1:` with
  `s=[n:=0];t={0}` and no `n+=1`: also 110. Legendre's theorem (n is a sum of
  three squares iff n is not 4^a(8b + 7)) needs more bytes than the set
  lookup.
- Exact integer arithmetic and complete searches over the squares up to n,
  so the program is right for every n.
- About 178000 terms in 60 s here (up to 295264); t holds about k²/2 sums
  when s has k squares.
- The b-file has 10000 terms (up to a(10000) = 17584); the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 147 | first entry |
| 2026-11-07 | Python 3 | 110 | next square from `len(s)`, three-square test as `A^{n}>{n}` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000419), CC BY-SA 4.0.
