# A001059

> Number of doubly labeled heap-ordered trees.
> — [OEIS A001059](https://oeis.org/A001059)

Offset 0: 1, 1, 5, 59, 1263, 42713, 2094399, 140434335, 12340275539, …

### Python 3 — 100 bytes

```python
import math
a=[n:=1]
while[print(a[-1])]:a+=sum(math.comb(n,k)**2*a[k]*a[~k]for k in range(n)),;n+=1
```

**Why the formula**

- The trees are plane rooted trees with n non-root vertices and two
  independent heap orderings (labels 1..n increasing away from the root);
  with one ordering they are counted by (2n−1)!! (A001147, as the entry
  says).
- Cut off the subtree S hanging from the root's first child. If S has m
  vertices, the rest is a tree with n − m non-root vertices. In each
  ordering S receives some m-subset of the labels (its root must get the
  smallest), and both parts are again heap-ordered, so

  a(n) = Σ_m C(n, m)²·a(m−1)·a(n−m),

  which is Vladeta Jovovic's formula in the entry,
  **a(n) = Σ_k C(n, k)²·a(k)·a(n−1−k)**, after k = n − m.

**How it works**

- `a` holds a(0..n−1), so `a[~k]` is a(n−1−k); the new term is appended
  with `a+=…,` and printed by the next pass (`a[-1]`).
- `import math` plus `math.comb` is 1 byte under `from math import*` when
  `comb` is used once.

**Notes**

- Exact integer arithmetic, correct for every n.
- O(n) binomials per term: over 800 terms in 20 s; the bar is the whole
  b-file (101 terms) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 100 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001059), CC BY-SA 4.0.
