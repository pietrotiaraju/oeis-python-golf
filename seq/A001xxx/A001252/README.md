# A001252

> Number of permutations of order n with the length of longest run equal to 4.
> — [OEIS A001252](https://oeis.org/A001252)

Offset 1: 0, 0, 0, 2, 16, 134, 1164, 10982, 112354, 1245676, 14909340, 191916532, 2646100822, 38932850396, 609137502242, …

### Python 3 — 169 bytes

```python
P=lambda v,s=0:[s:=s+x for x in[0]+v]
S=lambda W:[P([*map(sum,zip(*W))][::-1]),*map(P,W[:-1])]
A=[[0]]*2+[[2]];B=[[0],[-2]]
while[print(sum(map(sum,A+B)))]:A=S(A);B=S(B)
```

**How it works**

- The program is [A001251](../A001251/)'s with k = 4. It counts the
  permutations whose runs (maximal monotone stretches, up or down) all
  have at most 4 elements, subtracts those with at most 3, and
  prints the difference.
- Layer `W[L−2][p]` counts prefixes that end at rank p in a rising run
  of L elements. Going down is handled by complement symmetry, which
  reverses a layer. `P` is the exclusive prefix sum, which turns layer
  L into layer L+1. The reversed total of all layers starts the new runs
  of 2 elements. The A001251 page has the details, including why the
  start of 2 in the top layer (−2 for the k − 1 system) makes the sum of
  all layers the exact count.

**Notes**

- The whole b-file (450 terms) prints in under a second.
- [A001251](../A001251/) and [A001253](../A001253/) are k = 3 and k = 5.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 169 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001252), CC BY-SA 4.0.
