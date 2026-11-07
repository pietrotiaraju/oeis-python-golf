# A000418

> Number of n-node rooted trees of height 7.
> — [OEIS A000418](https://oeis.org/A000418)

Offset 1: 0, 0, 0, 0, 0, 0, 0, 1, 7, 34, …

### Python 3 — 116 bytes

```python
L=[1]*8;n=0
while[print(L[-2]-L[-3])]:n-=7;exec('L+=sum(d*L[n-d-8]*sum(L[d::d])for d in range(n,0,7))//n,;'*6);L+=1,
```

Height is counted in edges, so a(n) counts rooted unlabeled trees with n
nodes whose longest root-to-leaf path has 7 edges.

**How it works**

- Let b_h(m) count rooted trees with m + 1 nodes and height at most h.
  Removing the root leaves a multiset of subtrees of height at most
  h − 1, so Σ_m b_h(m)xᵐ = Π_{k≥1} (1 − xᵏ)^(−b_(h−1)(k−1)), and by
  logarithmic differentiation (as in [A000041](../A000041/))
  m·b_h(m) = Σ_{k=1}^{m} k·b_(h−1)(k−1)·Σ_{j≥1} b_h(m − jk).
  b_1(m) = 1 (the star), and a(n) = b_7(n−1) − b_6(n−1).
- One list holds everything: a leading 1, then for each m the seven
  entries b_2(m), …, b_7(m), b_1(m) = 1. The string run six times by
  `exec` appends b_2(m), …, b_7(m) in turn, and `L+=1,` adds the
  constant b_1(m).
- With n = −7m and d = −7k, while b_h(m) is being computed the list ends
  just before its slot, so `L[d::d]` steps back 7k entries at a time
  through b_h(m−k), b_h(m−2k), … (the leading 1 is never on that path).
  The weight b_(h−1)(k−1) sits one slot earlier in row k − 1, which is
  the same offset `n-d-8` from the end in every pass. For h = 2 that slot
  is the constant b_1(k−1) = 1 of the row before, and for k = 1 it is the
  leading 1, which is why the list starts with it.
- The factors 7 in d and n cancel in the exact division `//n`.
  `L[-2]-L[-3]` is b_7(m) − b_6(m) = a(m+1); the start `L=[1]*8` is the
  leading 1 and row 0, so the first print is a(1) = 0.

**Notes**

- The previous record (129 bytes) used six slots per row and an index
  `(-d-5+h)*(h<5)` that sends the bottom layer to the constant `L[0]`.
  The constant slot makes the weight index uniform, and then `exec`
  replaces `for h in range(6):` and its line break. The same loop with
  `for h in[1]*6:` on its own line is 123 bytes. Six slots per row with
  the weight `L[n-d-7]**h` (h = 0 in the first pass of each row, so the
  bottom weight is 1) needs a leading 0, which the slices then reach, and
  is 125 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 200 terms (up to a(200)) and prints in about 0.4 s; the
  bar is 200 terms in 60 s. Here about 2400 terms print in 60 s.
- a(n) has about 560 digits at n = 1500, so the 4300-digit limit is far
  beyond the terms the program reaches in practice.
- [A000235](../A000235/) and [A000299](../A000299/) interleave two and
  three height layers in the same way.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 129 | first entry |
| 2026-11-07 | Python 3 | 116 | constant slot for the stars, six passes by `exec` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000418), CC BY-SA 4.0.
