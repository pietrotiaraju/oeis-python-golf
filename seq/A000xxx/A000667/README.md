# A000667

> Boustrophedon transform of all-1's sequence.
> — [OEIS A000667](https://oeis.org/A000667)

Offset 0: 1, 2, 4, 9, 24, 77, 294, 1309, 6664, 38177, 243034, 1701909, 13001604, 107601977, 959021574, …

### Python 3 — 57 bytes

```python
r=[t:=1]
while[print(t)]:r=[t:=t+x for x in[1-t]+r[::-1]]
```

**How it works**

- With u = 1, 1, 1, …, the boustrophedon transform of u is b(n) = T(n,n) in the triangle
  T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and Young).
  Row n is the running sums of u(n) followed by row n−1 read backwards,
  exactly the triangle of [A000111](../A000111/), which is the transform of
  1, 0, 0, 0, …

  ```
  1
  1  2
  1  3  4
  1  5  8  9
  1 10 18 23 24
  ```
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `1-t` brings it to 1, the row's first entry; then it adds the
  old row reversed. When the comprehension ends, `t` is the new row's last
  entry, the next term, which the `while` header prints.
- `r=[t:=1]` is row 0. This is A000111's program with `[1-t]` in place of
  `[-t]`: one byte for the whole sequence of ones.

**Notes**

- The same template gives the other transforms in this group:
  [A000674](../A000674/) (`2-t`), [A000660](../A000660/) (`len(r)-t`),
  [A000697](../A000697/) (`len(r)**2-t`) and, with a captured Fibonacci
  pair, [A000687](../A000687/).
- The e.g.f. is exp(x)·(sec x + tan x), so a(n) = Σ C(n,k)·A000111(n−k);
  the values were checked against this for every printed term.
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(1660); the 1660 terms
  before it print in about a second.
- The b-file has 486 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 57 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000667), CC BY-SA 4.0.
