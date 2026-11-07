# A000756

> Boustrophedon transform of sequence 1,1,0,0,0,0,...
> — [OEIS A000756](https://oeis.org/A000756)

Offset 0: 1, 2, 3, 5, 13, 41, 157, 699, 3561, 20401, 129881, 909523, 6948269, 57504201, 512516565, …

### Python 3 — 60 bytes

```python
r=[t:=1]
while[print(t)]:r=[t:=t+x for x in[1//t-t]+r[::-1]]
```

**How it works**

- With u = 1, 1, 0, 0, 0, … (e.g.f. 1 + x, so b has e.g.f.
  (1 + x)·(sec x + tan x)),
  the boustrophedon transform of u is b(n) = T(n,n) in the
  triangle T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and
  Young). Row n is the running sums of u(n) followed by row n−1 read
  backwards, exactly the triangle of [A000111](../A000111/), which is the
  transform of 1, 0, 0, 0, …
- The first element is `1//t-t`. Before row 1, t = a(0) = 1, so `1//t` is 1
  = u(1); after that t = a(n−1) ≥ 2 (a(n) = E(n) + n·E(n−1) ≥ 2 for n ≥ 1),
  so `1//t` is 0 and every later row starts with u = 0, as in
  [A000111](../A000111/).
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `1//t-t` brings it to the new row's first entry u; then it adds the old row
  reversed. When the comprehension ends, `t` is the new row's last entry,
  the next term, which the `while` header prints.

**Notes**

- `(t<2)-t` is 1 byte longer, `t>1and-t` 2 bytes.
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
| 2026-11-07 | Python 3 | 60 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000756), CC BY-SA 4.0.
