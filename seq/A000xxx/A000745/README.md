# A000745

> Boustrophedon transform of squares.
> — [OEIS A000745](https://oeis.org/A000745)

Offset 0: 1, 5, 18, 57, 180, 617, 2400, 10717, 54544, 312353, 1988104, 13921501, 106350816, 880162337, 7844596536, …

### Python 3 — 67 bytes

```python
t=n=1;r=[1]
while[print(t)]:n+=1;r=[t:=t+x for x in[n*n-t]+r[::-1]]
```

**How it works**

- With u = 1, 4, 9, 16, …, the boustrophedon transform of u is b(n) = T(n,n) in the
  triangle T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and
  Young). Row n is the running sums of u(n) followed by row n−1 read
  backwards, exactly the triangle of [A000111](../A000111/), which is the
  transform of 1, 0, 0, 0, …
  Here u(n) = (n+1)², the squares from 1 (e.g.f. exp(x)(x² + 3x + 1)), so
  a(1) = 4 + 1 = 5.
- `n` is bumped before each pass, so the pass that builds row m has
  n = m + 1 and first entry `n*n`.
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `n*n-t` brings it to the new row's first entry u; then it adds the old row
  reversed. When the comprehension ends, `t` is the new row's last entry,
  the next term, which the `while` header prints.

**Notes**

- `(len(r)+1)**2` in place of the counter is 1 byte longer, and
  `r=[t:=1];n=2` with `;n+=1` after the pass is 1 byte longer than
  `t=n=1;r=[1]` with `n+=1;` before it.
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
| 2026-11-07 | Python 3 | 67 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000745), CC BY-SA 4.0.
