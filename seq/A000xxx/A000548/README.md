# A000548

> Squares that are not the sum of 2 nonzero squares.
> — [OEIS A000548](https://oeis.org/A000548)

Offset 1: 1, 4, 9, 16, 36, 49, 64, 81, 121, 144, …

### Python 3 — 63 bytes

```python
S={n:=0}
while[S&{n*n-s for s in S}or print(n*n)]:S|={n*n};n+=1
```

**How it works**

- When n² is tested, `S` holds the squares 0, 1, 4, …, (n − 1)². The set
  `{n*n-s for s in S}&S` is empty exactly when n² is not x² + y² with x, y ≥ 1:
  such x and y are below n, so x², y² ∈ S; conversely an element n² − s = t
  with s, t ∈ S has s, t ≥ 1, because s = 0 would give t = n² ∉ S.
- An empty set is falsy, so `S&{…}or print(n*n)` prints n² exactly then.
  The `print` sits in the loop condition: `[None]` or `[{…}]` is a non-empty
  list, so the loop never ends.
- The body adds n² to `S` and moves on. The first test runs at n = 0 with
  S = {0}, where the intersection is {0}, so nothing is printed and the
  output starts at 1.

**Notes**

- Other versions: rebuilding the set each time with
  `S={k*k for k in range(n)}` is 76 bytes; growing `r=[1]` in a `for n in r:`
  loop and intersecting `{n*n-k*k for k in r}&{k*k for k in r}` is 75; the
  `isqrt` square test over k = 1, …, n − 1 was 99 bytes.
- Exact integer arithmetic, so the program is right for every n. (The
  numbers printed are the n² where n has no prime factor ≡ 1 (mod 4), but the
  program does not use that.)
- Each term costs O(n) set operations: the whole b-file (1000 terms, up to
  2537²) prints in about 1.3 s here. The b-file has 1000 terms; the bar is 300
  terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 103 | first entry |
| 2026-11-06 | Python 3 | 99 | reuse the square residual and increment in the loop condition |
| 2026-11-07 | Python 3 | 63 | set of smaller squares, empty intersection as the test |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000548), CC BY-SA 4.0.
