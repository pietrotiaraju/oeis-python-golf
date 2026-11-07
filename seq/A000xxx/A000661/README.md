# A000661

> Shifts 2 places left under boustrophedon transform.
> — [OEIS A000661](https://oeis.org/A000661)

Offset 0: 1, 0, 1, 1, 2, 6, 17, 62, 259, 1230, 6592, 39313, 258575, 1860318, 14538245, 122670593, 1111715644, …

### Python 3 — 63 bytes

```python
t,u,*r=0,1
while[print(u)]:u,r=t,[t:=t+x for x in[u-t]+r[::-1]]
```

**How it works**

- The sequence a is its own boustrophedon transform shifted by two:
  B(a)(n) = a(n+2), with a(0) = 1 and a(1) = 0 from the OEIS data. B(a)(n)
  only uses a(0), …, a(n), so this fixes every term. With u = a,
  the boustrophedon transform of u is b(n) = T(n,n) in the triangle
  T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and Young).
  Row n is the running sums of u(n) followed by row n−1 read backwards,
  exactly the triangle of [A000111](../A000111/), which is the transform of
  1, 0, 0, 0, …
- So row n starts with a(n) and ends with a(n+2): the first entry of each
  row is the last entry of the row two before.

  ```
  1                 a(2) = 1
  0  1              a(3) = 1
  1  2  2           a(4) = 2
  1  3  5  6        a(5) = 6
  2  8 13 16 17     a(6) = 17
  ```
- `t` is the last entry of the newest row and `u` the one before it, the
  next row's first entry; the program prints `u`. In `u,r=t,[…]` the old
  `t` is taken before the comprehension changes it, so after the pass `u`
  moves up by one row. In the comprehension `[u-t]` brings the running sum
  `t` to `u`, then the old row is added backwards.
- `t,u,*r=0,1` starts with the empty row −1: `u` = a(0) = 1 and `t` = a(1) = 0.

**Notes**

- G. W. Hill (1886) gives the e.g.f. equation A″(x) = (sec x + tan x)·A(x),
  which is the same statement; the values were checked against it for
  every printed term.
- The walrus swap `r=[…for x in[u-(u:=t)]+r[::-1]]` is not allowed (no
  walrus in a comprehension's iterable), and would be 1 byte longer anyway.
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(1662); the 1662 terms
  before it print in about a second.
- The b-file has 481 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 63 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000661), CC BY-SA 4.0.
