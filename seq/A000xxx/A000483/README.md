# A000483

> Associated Stirling numbers: second-order reciprocal Stirling numbers (Fekete) a(n) = [[n, 3]]. The number of 3-orbit permutations of an n-set with at least 2 elements in each orbit.
> — [OEIS A000483](https://oeis.org/A000483)

Offset 6: 15, 210, 2380, 26432, 303660, 3678840, 47324376, 647536032, 9418945536, …

### Python 3 — 73 bytes

```python
z=y=Y=0;f=1;n=3
while[z>0==print(z)]:z,y,Y,f=n*(z+Y),n*(y+f),y,f*~-n;n+=1
```

**How it works**

- Let [[n,k]] count the permutations of [n] with k cycles, all of
  length ≥ 2. The element n either goes into a cycle of a permutation of
  [n−1] (after one of n − 1 elements) or forms a 2-cycle with one of the
  n − 1 others, so [[n,k]] = (n−1)·([[n−1,k]] + [[n−2,k−1]]).
- Column 1 is [[n,1]] = (n−1)! for n ≥ 2. At the top of the loop the state
  is z = [[n,3]], y = [[n,2]], Y = [[n−1,2]] and f = [[n−1,1]] = (n−2)!,
  and the tuple assignment moves it to n + 1:
  z ← n(z + Y), y ← n(y + f), Y ← y, f ← (n−1)·f (`f*~-n`).
- The start n = 3 has z = y = Y = 0 and f = 1! = 1. Three cycles of
  length ≥ 2 need n ≥ 6, so z stays 0 until then, and `z>0==print(z)`
  prints only from a(6) = 15 on: the chained comparison evaluates
  `0==print(z)` only when z > 0.

**Notes**

- The previous record, 101 bytes, kept all rows in a flat list.
  The e.g.f. −(x + log(1−x))³/6 gives
  a(n) = (n!/6)·Σ 1/(ijk) over i + j + k = n with i, j, k ≥ 2, and the
  double sum `sum(F//i//j//(n-i-j)…)//6` with F = n! is 100 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 195 terms (up to a(200)); the bar is the whole b-file in
  60 s. It prints in a fraction of a second.
- a(n) first has more than 4300 digits at n = 1559, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 101 | first entry |
| 2026-11-07 | Python 3 | 73 | three columns with a one-row lag in a tuple update |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000483), CC BY-SA 4.0.
