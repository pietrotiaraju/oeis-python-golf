# A000737

> Boustrophedon transform of natural numbers, cf. A000027.
> — [OEIS A000737](https://oeis.org/A000737)

Offset 0: 1, 3, 8, 21, 60, 197, 756, 3367, 17136, 98153, 624804, 4375283, 33424512, 276622829, 2465449252, …

### Python 3 — 62 bytes

```python
r=[t:=1]
while[print(t)]:r=[t:=t+x for x in[r[0]+1-t]+r[::-1]]
```

**How it works**

- With u = 1, 2, 3, 4, …, the boustrophedon transform of u is b(n) = T(n,n) in the
  triangle T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and
  Young). Row n is the running sums of u(n) followed by row n−1 read
  backwards, exactly the triangle of [A000111](../A000111/), which is the
  transform of 1, 0, 0, 0, …
  Here u(n) = n + 1 (e.g.f. (1 + x)·exp(x)).
- Every row starts with its u, so the next u is the old row's first entry
  plus one, `r[0]+1`.
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `r[0]+1-t` brings it to the new row's first entry u; then it adds the old row
  reversed. When the comprehension ends, `t` is the new row's last entry,
  the next term, which the `while` header prints.

**Notes**

- `len(r)+1` is 2 bytes longer; `-~r[0]-t` and `r[0]-~-t` tie.
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
| 2026-11-07 | Python 3 | 62 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000737), CC BY-SA 4.0.
