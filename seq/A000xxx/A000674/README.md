# A000674

> Boustrophedon transform of 1, 2, 2, 2, 2, ...
> — [OEIS A000674](https://oeis.org/A000674)

Offset 0: 1, 3, 7, 16, 43, 138, 527, 2346, 11943, 68418, 435547, 3050026, 23300443, 192835698, 1718682167, …

### Python 3 — 57 bytes

```python
r=[t:=1]
while[print(t)]:r=[t:=t+x for x in[2-t]+r[::-1]]
```

**How it works**

- With u = 1, 2, 2, 2, …, the boustrophedon transform of u is b(n) = T(n,n) in the triangle
  T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and Young).
  Row n is the running sums of u(n) followed by row n−1 read backwards,
  exactly the triangle of [A000111](../A000111/), which is the transform of
  1, 0, 0, 0, …

  ```
  1
  2  3
  2  5  7
  2  9 14 16
  2 18 32 41 43
  ```
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, so the first element
  `2-t` brings it to 2, the row's first entry; then it adds the
  old row reversed. When the comprehension ends, `t` is the new row's last
  entry, the next term, which the `while` header prints.
- `r=[t:=1]` is row 0 (u(0) = 1); every later row starts at 2.

**Notes**

- Same template as [A000667](../A000667/) (all ones, `1-t`) and
  [A000111](../A000111/) (`-t`).
- The e.g.f. is (sec x + tan x)·(2 exp(x) − 1); the values were checked
  against it for every printed term.
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(1660); the 1660 terms
  before it print in about a second.
- The b-file has 401 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 57 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000674), CC BY-SA 4.0.
