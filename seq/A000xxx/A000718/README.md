# A000718

> Boustrophedon transform of triangular numbers 1,1,3,6,10,...
> — [OEIS A000718](https://oeis.org/A000718)

Offset 0: 1, 2, 6, 20, 65, 226, 883, 3947, 20089, 115036, 732171, 5126901, 39165917, 324138010, 2888934623, …

### Python 3 — 70 bytes

```python
t=c=1;r=[1]
while[print(t)]:r=[t:=t+x for x in[c-t]+r[::-1]];c+=len(r)
```

**How it works**

- With u = 1, 1, 3, 6, 10, …, the boustrophedon transform of u is b(n) = T(n,n) in the
  triangle T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and
  Young). Row n is the running sums of u(n) followed by row n−1 read
  backwards, exactly the triangle of [A000111](../A000111/), which is the
  transform of 1, 0, 0, 0, …
  Here u(0) = 1 and u(n) = n(n+1)/2 for n ≥ 1 (the e.g.f. in the entry is
  (sec x + tan x)(exp(x)(x + x²/2) + 1)).
- `c` holds the next u. It starts at u(1) = 1; the pass that builds row m
  leaves m+1 entries in `r`, so `c+=len(r)` turns m(m+1)/2 into
  (m+1)(m+2)/2.
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `c-t` brings it to the new row's first entry u; then it adds the old row
  reversed. When the comprehension ends, `t` is the new row's last entry,
  the next term, which the `while` header prints.

**Notes**

- The closed form `len(r)*-~len(r)//2` in place of `c` is 3 bytes longer.
  `r[0]+len(r)` (the old u plus n) would be shorter, but it is wrong for
  row 1: u(0) = 1 is not the triangular number 0.
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
| 2026-11-07 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000718), CC BY-SA 4.0.
