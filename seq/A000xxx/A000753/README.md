# A000753

> Boustrophedon transform of Catalan numbers.
> — [OEIS A000753](https://oeis.org/A000753)

Offset 0: 1, 2, 5, 16, 59, 243, 1101, 5461, 29619, 175641, 1137741, 8031838, 61569345, 510230087, 4549650423, …

### Python 3 — 78 bytes

```python
r=[t:=1]
while[print(t)]:r=[t:=t+x for x in[4*r[0]+6*r[0]//~len(r)-t]+r[::-1]]
```

**How it works**

- With u = C(n) = 1, 1, 2, 5, 14, … (the Catalan numbers from C(0)),
  the boustrophedon transform of u is b(n) = T(n,n) in the
  triangle T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and
  Young). Row n is the running sums of u(n) followed by row n−1 read
  backwards, exactly the triangle of [A000111](../A000111/), which is the
  transform of 1, 0, 0, 0, …
- Every row starts with its u, and the old row (row n−1) has n entries.
  C(n) = C(n−1)·(4n−2)/(n+1) = 4·C(n−1) − 6·C(n−1)/(n+1), and
  `~len(r)` = −(n+1), so `4*r[0]+6*r[0]//~len(r)` is C(n). The quotient is
  exact: 6·C(n−1)/(n+1) = 4·C(n−1) − C(n) is an integer, so flooring by the
  negative divisor just flips its sign.
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `…//~len(r)-t` brings it to the new row's first entry u; then it adds the old row
  reversed. When the comprehension ends, `t` is the new row's last entry,
  the next term, which the `while` header prints.

**Notes**

- `-6*r[0]//-~len(r)` is 1 byte longer; a separate Catalan variable
  updated after the row (as in [A000736](../A000736/)) is 3 bytes longer.
- The values were checked for every printed term against
  b(n) = Σₖ C(n,k)·E(n−k)·u(k), the e.g.f. product (sec x + tan x)·U(x), with
  E = [A000111](../A000111/) computed from 2E(n+1) = Σₖ C(n,k)E(k)E(n−k).
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(1660); the 1660 terms
  before it print in about two seconds.
- The b-file has 401 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 78 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000753), CC BY-SA 4.0.
