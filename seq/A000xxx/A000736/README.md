# A000736

> Boustrophedon transform of Catalan numbers 1, 1, 1, 2, 5, 14, ...
> — [OEIS A000736](https://oeis.org/A000736)

Offset 0: 1, 2, 4, 10, 32, 120, 513, 2455, 13040, 76440, 492231, 3465163, 26530503, 219754535, 1959181266, …

### Python 3 — 78 bytes

```python
t=c=1;r=[1]
while[print(t)]:r=[t:=t+x for x in[c-t]+r[::-1]];c=4*c-6*c//len(r)
```

**How it works**

- With u = 1, 1, 1, 2, 5, 14, …, the boustrophedon transform of u is b(n) = T(n,n) in the
  triangle T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and
  Young). Row n is the running sums of u(n) followed by row n−1 read
  backwards, exactly the triangle of [A000111](../A000111/), which is the
  transform of 1, 0, 0, 0, …
  Here u(0) = 1 and u(n) = C(n−1), the Catalan numbers shifted one place.
- `c` holds the next u, starting at C(0) = 1. After the pass that builds
  row n+1, `r` has n+2 entries, and
  C(n+1) = C(n)·(4n+2)/(n+2) = 4C(n) − 6C(n)/(n+2); the division is exact
  because 6C(n)/(n+2) = 4C(n) − C(n+1). This is the
  [A000108](../A000108/) step with n+2 = `len(r)`.
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `c-t` brings it to the new row's first entry u; then it adds the old row
  reversed. When the comprehension ends, `t` is the new row's last entry,
  the next term, which the `while` header prints.

**Notes**

- The old first entry `r[0]` already holds C(n−1) for n ≥ 1, so
  `4*r[0]-6*r[0]//len(r)` would need no `c`, but it is wrong for row 1,
  where u(1) = u(0) = 1.
- `t=c=1;r=[1]` is a byte shorter than `r=[t:=1];c=1`.
- The values were checked for every printed term against
  b(n) = Σₖ C(n,k)·E(n−k)·u(k), the e.g.f. product (sec x + tan x)·U(x), with
  E = [A000111](../A000111/) computed from 2E(n+1) = Σₖ C(n,k)E(k)E(n−k).
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(1660); the 1660 terms
  before it print in about a second.
- The b-file has 401 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 78 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000736), CC BY-SA 4.0.
