# A001251

> Number of permutations of order n with the length of longest run equal to 3.
> — [OEIS A001251](https://oeis.org/A001251)

Offset 1: 0, 0, 2, 12, 70, 442, 3108, 24216, 208586, 1972904, 20373338, 228346522, 2763212980, 35926266244, 499676669254, …

### Python 3 — 161 bytes

```python
P=lambda v,s=0:[s:=s+x for x in[0]+v]
S=lambda W:[P([*map(sum,zip(*W))][::-1]),*map(P,W[:-1])]
A=[[0],[2]];B=[[-2]]
while[print(sum(map(sum,A+B)))]:A=S(A);B=S(B)
```

**How it works**

- A run here is a maximal monotone stretch, up or down. A001250 has
  longest run 2: those are the alternating permutations. So "longest run
  = 3" means that some run has 3 elements but no 4 consecutive elements
  are monotone. The program counts permutations whose runs all have at
  most k elements, and prints (k = 3 count) − (k = 2 count).
- Permutations are built left to right. A prefix of length m is recorded
  by the rank p of its last element among the prefix, together with the
  length L of its current run. A new element of rank q goes up when q > p
  and down when q ≤ p. Taking complements (x → m+1−x) swaps up with down
  and p with m−1−p. So only rising runs are stored. Layer `W[L−2][p]`
  counts prefixes whose current run is rising, has L elements and ends at
  rank p. A falling run is a reversed rising layer.
- One step `S`:
  - A rising run of L elements grows to L + 1 by going up. That sends
    layer L to layer L+1 through the exclusive prefix sum
    `P` (new[q] = Σ_{p<q} old[p]). Layer k is dropped, because k+1 is
    too long.
  - Any falling run turns into a new rising run of 2 elements. That is
    `P` of the reversed sum of all layers.
  - Going down is the mirror image of these two moves, so it needs no
    code.
- The start is m = 1, with weight 2 in the top layer (L = k). The top
  layer cannot grow, so the 2 only feeds the new run of 2 elements, and
  only through the reversed total. That gives `[0,2]`: each two-element
  prefix is stored once for itself and once for its mirror image. From
  m = 2 on, every stored weight is twice the number of rising prefixes,
  which is rising plus falling prefixes. So the sum of all layers is
  exactly the number of permutations. At m = 1 the sum is 2 for both k and
  k − 1. The k − 1 system starts at −2, so one `sum` prints the
  difference, and a(1) = 0.

**Notes**

- A step costs m·k additions, so the whole b-file (450 terms) prints in
  under a second.
- [A001252](../A001252/) and [A001253](../A001253/) are the same program
  with k = 4 and 5.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 161 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001251), CC BY-SA 4.0.
