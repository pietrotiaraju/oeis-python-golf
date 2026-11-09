# A001384

> Number of n-node trees of height at most 4.
> — [OEIS A001384](https://oeis.org/A001384)

Offset 0: 1, 1, 1, 2, 4, 9, 19, 42, 89, 191, 402, 847, 1763, 3667, 7564, 15564, 31851, …

The trees are rooted (the data are the rooted trees of
[A000081](../../A000xxx/A000081/) minus the tall ones: 20 − 1 = 19 on six
nodes), and a(0) = 1 is the entry's convention. The entry's formula: the Euler
transform of [A001383](../A001383/) shifted right.

### Python 3 — 115 bytes

```python
L=[1]*6;n=0
while[print(L[-6])]:
 n-=3
 for h in 1,1,0:L+=sum(d*L[n-d-2]**h*sum(L[d:2:d])for d in range(n,0,3))//n,
```

**How it works**

- **Forests by height.** Let Fₕ count rooted forests of height at most h, so
  F₁ = p (partitions, [A000041](../../A000xxx/A000041/)) and Fₕ is the Euler
  transform of Fₕ₋₁(k − 1) (a tree of height at most h on k nodes is a root
  over a forest of height at most h − 1 on k − 1 nodes). Then
  a(m + 1) = F₃(m).
- **Three recurrences.** Each series follows the log-derivative recurrence
  m·F(m) = Σₖ k·w(k)·Σⱼ F(m − jk) (k = 1…m, j ≥ 1), with weight
  w(k) = F₂(k−1) for F₃, p(k−1) for F₂ and 1 for p: the layout of
  [A000299](../../A000xxx/A000299/) (height exactly 4 = F₃ − F₂).
- **One list.** `L` = [1, 1, 1, F₃(0), F₂(0), p(0), F₃(1), …]: three dummy
  entries, then the series interleaved. Each round appends F₃(m), F₂(m), p(m)
  with n = −3m; `d` = −3k, and `L[d:2:d]` reads the current series at
  m − k, m − 2k, …, the stop `2` keeping the dummies out.
- **The weight** `L[n-d-2]` is the same negative index in every pass, and it
  is always the next series at k − 1; `**h` with h = 0 turns it into 1 for
  the partitions.
- **The print.** `L[-6]` is F₃(m − 1) = a(m) after round m; before the first
  round it is the first dummy, the conventional a(0) = 1.

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n.
- The whole b-file (201 terms) prints in about 0.1 s; the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 115 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001384), CC BY-SA 4.0.
