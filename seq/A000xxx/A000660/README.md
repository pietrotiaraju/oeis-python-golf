# A000660

> Boustrophedon transform of 1,1,2,3,4,5,...
> — [OEIS A000660](https://oeis.org/A000660)

Offset 0: 1, 2, 5, 14, 41, 136, 523, 2330, 11857, 67912, 432291, 3027166, 23125673, 191389108, 1705788659, …

### Python 3 — 62 bytes

```python
r=[t:=1]
while[print(t)]:r=[t:=t+x for x in[len(r)-t]+r[::-1]]
```

**How it works**

- With u = 1, 1, 2, 3, 4, …, the boustrophedon transform of u is b(n) = T(n,n) in the triangle
  T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and Young).
  Row n is the running sums of u(n) followed by row n−1 read backwards,
  exactly the triangle of [A000111](../A000111/), which is the transform of
  1, 0, 0, 0, …
- Row n−1 has n entries, so u(n) = n for n ≥ 1 is just `len(r)` when row n
  is built; row 0, `r=[t:=1]`, supplies u(0) = 1.
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `len(r)-t` brings it to u(n), the row's first entry; then it adds the
  old row reversed. When the comprehension ends, `t` is the new row's last
  entry, the next term, which the `while` header prints.

**Notes**

- A counter (`n=t=1;r=[1]` … `n-t` … `;n+=1`) costs 3 bytes more than
  `len(r)`.
- Same template as [A000667](../A000667/), [A000674](../A000674/) and
  [A000697](../A000697/).
- The e.g.f. is (x·exp(x) + 1)·(sec x + tan x); the values were checked
  against it for every printed term.
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
Sequences](https://oeis.org/A000660), CC BY-SA 4.0.
