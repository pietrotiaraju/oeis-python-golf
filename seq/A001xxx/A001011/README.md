# A001011

> Number of ways to fold a strip of n blank stamps.
> — [OEIS A001011](https://oeis.org/A001011)

Offset 1: 1, 1, 2, 5, 14, 38, 120, 353, 1148, 3527, 11622, 36627, 121622, …

With blank stamps, a folding and the one seen from the other end of the
strip are the same, and so is the folding with the pile turned upside
down. So a(n) counts the foldings of a strip of n labeled stamps
([A000136](../A000136/)) up to renumbering the stamps from the other end,
turning the pile over, or both.

### Python 3 — 203 bytes

```python
L=[[0]]
while[print(sum(1+(q[::-1]==[len(q)+~v for v in q])for q in L)+2>>2)]:L=[[x+1,*[v+(v>x)for v in(p,*r)]]for p,*r in L for x in(-1,p,*r)if all((x<c)^(x<d)==(p<c)^(p<d)for c,d in zip(*[iter(r)]*2))]
```

**How it works**

- Burnside's lemma for the group of these four moves: a(n) is the average
  number of foldings each move leaves alone. The identity fixes all
  A000136(n) foldings. For n ≥ 2 renumbering alone or turning over alone
  fixes none (two stamps would share a height), and doing both fixes the
  symmetric foldings, h(j) + h(n+1−j) = n+1 ([A001010](../A001010/)). So
  a(n) = (A000136(n) + A001010(n))/4, the formula in the OEIS entry; for
  n = 1 all four moves fix the single folding, and `+2>>2` turns
  (1 + 1)/4 into the right 1 while leaving the multiples of 4 alone.
- `L` holds every folding of the current length as a list of heights
  0 … k−1, newest stamp first. It grows as in [A000136](../A000136/): the
  new stamp goes just above `x`, a height in the pile or −1 for the
  bottom, gets height x + 1, and the old heights above `x` move up one
  (`v+(v>x)`). Only the new crease can break the rule that creases on the
  same edge must not interleave, and `(x<c)^(x<d)==(p<c)^(p<d)` checks it
  on the old heights, where the new stamp sits at x + ½.
- With heights 0 … k−1 a folding is symmetric when its reverse is its
  complement: `q[::-1]==[len(q)+~v for v in q]`. Each folding adds 1, or 2
  if it is symmetric.

**Notes**

- Exact integers; correctness rests on the folding criterion (Koehler
  1968, Lunnon 1968) and Burnside's lemma.
- The list holds all A000136(n) foldings, about 3.5 times more per step:
  13 terms print in about 12 s here, and building the next list passes
  300 MB about 15 s later. So the bar is 10 terms in 15 s (the b-file
  has 45).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 203 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001011), CC BY-SA 4.0.
