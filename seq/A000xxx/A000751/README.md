# A000751

> Boustrophedon transform of partition numbers.
> — [OEIS A000751](https://oeis.org/A000751)

Offset 0: 1, 2, 5, 14, 42, 143, 555, 2485, 12649, 72463, 461207, 3229622, 24671899, 204185616, 1819837153, …

### Python 3 — 117 bytes

```python
n=0;r=a=[t:=1]
while[print(t)]:n-=1;r=[t:=t+x for x in[sum(d*sum(a[d::d])for d in range(n,0))//n-t]+r[::-1]];a+=r[:1]
```

**How it works**

- With u = p(n) = 1, 1, 2, 3, 5, 7, … (the partition numbers from p(0)),
  the boustrophedon transform of u is b(n) = T(n,n) in the
  triangle T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and
  Young). Row n is the running sums of u(n) followed by row n−1 read
  backwards, exactly the triangle of [A000111](../A000111/), which is the
  transform of 1, 0, 0, 0, …
- p(n) comes from Euler's recurrence n·p(n) = Σₖ σ(k)·p(n−k), as in
  [A000041](../A000041/): `a` holds p(0), …, p(|n|−1) and the counter `n`
  runs negative, so `a[d::d]` for d = −1, −2, … walks back from p(n+d) in
  steps of d and `d*sum(a[d::d])` collects the σ(k) weights; `//n` divides
  by the (negative) index.
- The new p(n) is computed straight into the first element of the new row,
  and `a+=r[:1]` then appends the new row's first entry, which is p(n). At
  the start `r` and `a` are the same list [1], but `r` is rebound to the
  new row before `a+=` extends `a` in place.
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `…//n-t` brings it to the new row's first entry u; then it adds the old row
  reversed. When the comprehension ends, `t` is the new row's last entry,
  the next term, which the `while` header prints.

**Notes**

- [A000733](../A000733/) (1 and then the partition numbers) uses `a[-1]`
  and appends the new p(n) after the row; here the row needs p(n) itself, and
  `a+=r[:1]` is 1 byte shorter than that order.
- The values were checked for every printed term against
  b(n) = Σₖ C(n,k)·E(n−k)·u(k), the e.g.f. product (sec x + tan x)·U(x), with
  E = [A000111](../A000111/) computed from 2E(n+1) = Σₖ C(n,k)E(k)E(n−k).
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(1660); the 1660 terms
  before it print in about three seconds.
- The b-file has 483 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 117 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000751), CC BY-SA 4.0.
