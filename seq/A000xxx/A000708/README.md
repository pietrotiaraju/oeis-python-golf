# A000708

> a(n) = E(n+1) - 2*E(n), where E(i) is the Euler number A000111(i).
> — [OEIS A000708](https://oeis.org/A000708)

Offset 0: -1, -1, 0, 1, 6, 29, 150, 841, 5166, 34649, 252750, 1995181, 16962726, 154624469, 1505035350, …

### Python 3 — 65 bytes

```python
r=[0,t:=1]
while[print(t-2*r[1])]:r=[t:=t+x for x in[-t]+r[::-1]]
```

**How it works**

- The Seidel–Entringer triangle of [A000111](../A000111/): row n is the
  running sums of 0 followed by row n−1 read backwards, and it ends with
  E(n).

  ```
  1
  0  1
  0  1  1
  0  1  2  2
  0  2  4  5  5
  ```

- Row n+1 starts 0, E(n) (its second entry is the first one read from row n,
  which is that row's last entry) and ends with E(n+1). So on row n+1,
  a(n) = `t-2*r[1]`.
- The program starts at row 1, `r=[0,t:=1]`, so that `r[1]` exists at the
  first print: a(0) = 1 − 2·1 = −1. The loop is the A000111 one: `t` runs
  along the new row as a walrus sum, the first element `-t` brings it to 0,
  then it adds the old row reversed and ends on the new row's last entry.

**Notes**

- The e.g.f. (1 − 2 cos x)/(1 − sin x) is (sec x + tan x)(sec x − 2), so a(n)
  is also the boustrophedon transform of −1, 0, 1, 0, 5, 0, 61, … (secant
  numbers minus 2 at n = 0), but generating those costs more than
  `-2*r[1]`.
- From row 2 on, every row ends with two equal entries, so the third entry
  of row n+1 is 2E(n) and `t-r[2]` would do, but not for n = 0, 1. A search
  over short starting rows, first-entry rules αt + β·r[0] + γ and prints
  t − r[1], t − r[2], r[1], … found no triangle that gives a(n) with fewer
  bytes.
- The values were checked against E(n+1) − 2E(n), with E computed from
  2E(n+1) = Σₖ C(n,k)E(k)E(n−k), for every printed term.
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(1659); the 1659 terms
  before it print in about a second.
- The b-file has 483 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 65 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000708), CC BY-SA 4.0.
