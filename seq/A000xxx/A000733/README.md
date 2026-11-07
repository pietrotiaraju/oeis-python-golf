# A000733

> Boustrophedon transform of partition numbers 1, 1, 1, 2, 3, 5, 7, ...
> — [OEIS A000733](https://oeis.org/A000733)

Offset 0: 1, 2, 4, 10, 30, 101, 394, 1760, 8970, 51368, 326991, 2289669, 17491625, 144760655, 1290204758, …

### Python 3 — 118 bytes

```python
n=0;r=a=[t:=1]
while[print(t)]:r=[t:=t+x for x in[a[-1]-t]+r[::-1]];n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- With u = 1, 1, 1, 2, 3, 5, 7, …, the boustrophedon transform of u is b(n) = T(n,n) in the
  triangle T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and
  Young). Row n is the running sums of u(n) followed by row n−1 read
  backwards, exactly the triangle of [A000111](../A000111/), which is the
  transform of 1, 0, 0, 0, …
  Here u(0) = 1 and u(n) = p(n−1), the partition numbers shifted one place
  (the array in the entry has row 3 starting with 2 = p(2)).
- `a` holds p(0), …, p(m−1) when row m is built, so u(m) is `a[-1]`. After
  the pass, the [A000041](../A000041/) step appends p(m) from
  m·p(m) = Σₖ σ(k)·p(m−k): with the negative counter n = −m, `a[d::d]` for
  d = n, …, −1 walks the list backwards from p(m+d) in steps of |d|, so
  `d*sum(a[d::d])` collects the divisor d of every k at once, and dividing
  by n fixes the sign.
- `r=a=[t:=1]` points both names at the same list [1], which is row 0 and
  also [p(0)]; the first pass rebinds `r` to a new list before `a+=…,`
  extends `a` in place.
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `a[-1]-t` brings it to the new row's first entry u; then it adds the old row
  reversed. When the comprehension ends, `t` is the new row's last entry,
  the next term, which the `while` header prints.

**Notes**

- `n=0;r=a=[t:=1]` is 3 bytes shorter than A000041's `*a,n=1,0` plus a
  separate `r=[t:=1]`.
- The values were checked for every printed term against
  b(n) = Σₖ C(n,k)·E(n−k)·u(k), the e.g.f. product (sec x + tan x)·U(x), with
  E = [A000111](../A000111/) computed from 2E(n+1) = Σₖ C(n,k)E(k)E(n−k).
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(1660); the 1660 terms
  before it print in about a second.
- The b-file has 483 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 118 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000733), CC BY-SA 4.0.
