# A000744

> Boustrophedon transform (second version) of Fibonacci numbers 1,1,2,3,...
> — [OEIS A000744](https://oeis.org/A000744)

Offset 0: 1, 2, 5, 14, 42, 144, 563, 2526, 12877, 73778, 469616, 3288428, 25121097, 207902202, 1852961189, …

### Python 3 — 68 bytes

```python
r=[t:=1]
while[print(t)]:r=[t:=t+x for x in[r[0]-(r*2)[-2]]+r[::-1]]
```

**How it works**

- With u = F(n+1) = 1, 1, 2, 3, 5, …, the boustrophedon transform of u is b(n) = T(n,n) in the
  triangle T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and
  Young). Row n is the running sums of u(n) followed by row n−1 read
  backwards, exactly the triangle of [A000111](../A000111/), which is the
  transform of 1, 0, 0, 0, …
  ("Second version": the Fibonacci numbers from F(1).)
- Row n is the running sums of u(n) and row n−1 reversed, so its last step
  adds the first entry of row n−1: u(n−1) = `r[-1]-r[-2]` = t − `r[-2]`
  for n ≥ 1. The next u is u(n) + u(n−1) = `r[0]` + t − `r[-2]`, so the
  first element, that minus t, is just `r[0]-r[-2]`: the triangle carries
  the Fibonacci recurrence by itself.
- Row 0 = [1] has no `r[-2]`. `(r*2)[-2]` is `r[-2]` for every longer row
  and `r[0]` = 1 for row 0, where the first element comes out 0, so row 1
  starts with t = 1 = u(1).
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so adding the first element
  `r[0]-(r*2)[-2]` gives the new row's first entry u; then it adds the old row
  reversed. When the comprehension ends, `t` is the new row's last entry,
  the next term, which the `while` header prints.

**Notes**

- [A000687](../A000687/)'s stored x (`f=0`, `(f:=x)`, `r[0]+f-t`) is 2 bytes
  longer.
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
| 2026-11-07 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000744), CC BY-SA 4.0.
