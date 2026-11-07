# A000738

> Boustrophedon transform (first version) of Fibonacci numbers 0,1,1,2,3,...
> — [OEIS A000738](https://oeis.org/A000738)

Offset 0: 0, 1, 3, 8, 25, 85, 334, 1497, 7635, 43738, 278415, 1949531, 14893000, 123254221, 1098523231, …

### Python 3 — 70 bytes

```python
r=[t:=0];f=1
while[print(t)]:r=[t:=t+(f:=x)for x in[r[0]+f-t]+r[::-1]]
```

**How it works**

- With u = F(n) = 0, 1, 1, 2, 3, 5, …, the boustrophedon transform of u is b(n) = T(n,n) in the
  triangle T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and
  Young). Row n is the running sums of u(n) followed by row n−1 read
  backwards, exactly the triangle of [A000111](../A000111/), which is the
  transform of 1, 0, 0, 0, …
  ("First version": the Fibonacci numbers from F(0) = 0, so a(0) = 0.)
- The Fibonacci step without a second state pair, as in
  [A000687](../A000687/): `(f:=x)` stores every x the row reads, and the
  last x read is the old row's first entry. So after the pass that builds
  row n+1, `r[0]` = u(n+1) and `f` = u(n), and the next u is `r[0]+f`.
  `f=1` is F(−1), which gives u(1) = 0 + 1.
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `r[0]+f-t` brings it to the new row's first entry u; then it adds the old row
  reversed. When the comprehension ends, `t` is the new row's last entry,
  the next term, which the `while` header prints.

**Notes**

- A row's last step adds the first entry of the row before, so on row n,
  u(n−1) = t − `r[-2]` and the first element shrinks to `r[0]-r[-2]` with
  no `f` at all; this is how [A000744](../A000744/) works. Here row 0 needs
  the sentinel F(−1) = 1, `r[0]-[-1,*r][-2]`, which ties at 70 bytes.
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
| 2026-11-07 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000738), CC BY-SA 4.0.
