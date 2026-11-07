# A000415

> Numbers that are the sum of 2 but no fewer nonzero squares.
> — [OEIS A000415](https://oeis.org/A000415)

Offset 1: 2, 5, 8, 10, 13, 17, 18, 20, 26, 29, …

### Python 3 — 82 bytes

```python
n=0;s={0}
while n:=n+1:s|={n}&{len(s)**2};n in s or{n-x for x in s}&s and print(n)
```

**How it works**

- These are the non-squares that are sums of two squares; for a
  non-square, any such representation has both squares nonzero.
- Before the update `s` holds 0 and the squares below n,
  {0, 1, 4, …, (j − 1)²} with (j − 1)² < n ≤ j². It has j elements, so
  `s|={n}&{len(s)**2}` adds n exactly when n = j² is a square, and
  `n in s` is then the square test.
- For a non-square n, `{n-x for x in s}&s` is non-empty exactly when
  n = x + y with x, y in `s`, i.e. when n is a sum of two squares (both
  below n). `n in s or …and print(n)` groups as
  `n in s or (… and print(n))`, so squares are skipped and the rest are
  printed when the intersection is non-empty.
- `while n:=n+1:` steps n in the header; n is never 0 there.

**Notes**

- [A000404](../A000404/) is the same program without the square test.
  Adding `len(s)**2==n or` to it instead is 88 bytes, and the counter
  version `n=k=1;s={1}` with `s|={k*k};k+=k*k<=n;` is 84.
- Exact integer arithmetic and a complete search over the squares below
  n, so the program is right for every n.
- A test costs about √n set operations: the whole b-file prints in about
  2 s here and about 110 000 terms in 60 s. The b-file has 10000 terms
  (up to a(10000) = 40445); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 106 | first entry |
| 2026-11-07 | Python 3 | 82 | set intersection, square test via `len(s)` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000415), CC BY-SA 4.0.
