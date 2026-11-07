# A000764

> Boustrophedon transform of Bell numbers.
> — [OEIS A000764](https://oeis.org/A000764)

Offset 0: 1, 2, 5, 16, 60, 258, 1247, 6686, 39371, 252688, 1756920, 13168178, 105949517, 911834394, 8367625793, …

### Python 3 — 83 bytes

```python
m=0;L=[t:=1]
while[print(t)]:L=[t:=t+x for x in[L[m]-t]+L[:m]+[0]+L[m:][::-1]];m+=1
```

**How it works**

- With u = B(n) = 1, 1, 2, 5, 15, … (the Bell numbers from B(0)),
  the boustrophedon transform of u is b(n) = T(n,n) in the
  triangle T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and
  Young). Row n is the running sums of u(n) followed by row n−1 read
  backwards, exactly the triangle of [A000111](../A000111/), which is the
  transform of 1, 0, 0, 0, …
- The Bell numbers come from Aitken's array, as in [A000110](../A000110/):
  each row starts with the last entry of the row above and then adds that
  row's entries one by one; row n starts with B(n) and ends with B(n+1).
- One list `L` holds Aitken row n−1 (n entries) followed by boustrophedon
  row n (n+1 entries), and `m` = n counts the passes. The new `L` is the
  running sums of B(n), Aitken row n−1, 0 and boustrophedon row n reversed:
  the first n+1 sums are Aitken row n, ending in B(n+1); the 0 repeats
  B(n+1) as the first entry of boustrophedon row n+1; the rest finish that
  row. So the two triangles share one walrus sum.
- B(n), the start of the Aitken part, is `L[m]`: the first entry of
  boustrophedon row n equals the last entry of Aitken row n−1. For n = 0
  the Aitken part is empty and `L[0]` is the 1 of row 0.
- At the start of a pass `t` still holds the last entry of the old
  boustrophedon row, so the first element `L[m]-t` brings it to B(n). When
  the comprehension ends, `t` is the last entry of the new boustrophedon
  row, the next term, which the `while` header prints.

**Notes**

- Two lists (an Aitken row with its own walrus `s`, then `[s-t]`) take 89
  bytes; `m=len(L)//2` instead of the counter is 3 bytes longer.
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
| 2026-11-07 | Python 3 | 83 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000764), CC BY-SA 4.0.
