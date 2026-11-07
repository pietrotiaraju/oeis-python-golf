# A000734

> Boustrophedon transform of 1,1,2,4,8,16,32,...
> — [OEIS A000734](https://oeis.org/A000734)

Offset 0: 1, 2, 5, 15, 49, 177, 715, 3255, 16689, 95777, 609875, 4270695, 32624329, 269995377, 2406363835, …

### Python 3 — 65 bytes

```python
t=p=1;r=[1]
while[print(t)]:r=[t:=t+x for x in[p-t]+r[::-1]];p*=2
```

**How it works**

- With u = 1, 1, 2, 4, 8, 16, …, the boustrophedon transform of u is b(n) = T(n,n) in the
  triangle T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and
  Young). Row n is the running sums of u(n) followed by row n−1 read
  backwards, exactly the triangle of [A000111](../A000111/), which is the
  transform of 1, 0, 0, 0, …
  Here u(0) = 1 and u(n) = 2ⁿ⁻¹ for n ≥ 1 (e.g.f. (1 + exp(2x))/2).
- `p` holds the next u: it starts at u(1) = 1 and doubles after every pass.
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `p-t` brings it to the new row's first entry u; then it adds the old row
  reversed. When the comprehension ends, `t` is the new row's last entry,
  the next term, which the `while` header prints.

**Notes**

- `2**~-len(r)` in place of `p` is 2 bytes longer. Doubling the old first
  entry, `2*r[0]`, would be shorter, but it is wrong for row 1, since
  u(1) = u(0).
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
| 2026-11-07 | Python 3 | 65 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000734), CC BY-SA 4.0.
