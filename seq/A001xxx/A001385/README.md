# A001385

> Number of n-node trees of height at most 5.
> — [OEIS A001385](https://oeis.org/A001385)

Offset 0: 1, 1, 1, 2, 4, 9, 20, 47, 108, 252, 582, 1345, 3086, 7072, 16121, 36667, …

The trees are rooted (the data are the rooted trees of
[A000081](../../A000xxx/A000081/) minus the tall ones: 48 − 1 = 47 on seven
nodes), and a(0) = 1 is the entry's convention.

### Python 3 — 117 bytes

```python
L=[1]*8;n=0
while[print(L[-8])]:
 n-=4
 for h in 1,1,1,0:L+=sum(d*L[n-d-3]**h*sum(L[d:3:d])for d in range(n,0,4))//n,
```

**How it works**

- **Forests by height.** Let Fₕ count rooted forests of height at most h, so
  F₁ = p (partitions, [A000041](../../A000xxx/A000041/)) and Fₕ is the Euler
  transform of Fₕ₋₁(k − 1): a tree of height at most h on k nodes is a root
  over a forest of height at most h − 1 on k − 1 nodes. Then
  a(m + 1) = F₄(m).
- **Four recurrences.** Each series follows the log-derivative recurrence
  m·F(m) = Σₖ k·w(k)·Σⱼ F(m − jk) (k = 1…m, j ≥ 1), with weight
  w(k) = Fₕ₋₁(k − 1) for Fₕ and 1 for p, as in [A001384](../A001384/) and
  [A000299](../../A000xxx/A000299/).
- **One list.** `L` = [1, 1, 1, 1, F₄(0), F₃(0), F₂(0), p(0), F₄(1), …]: four
  dummy entries, then the series interleaved. Each round appends F₄(m), F₃(m),
  F₂(m), p(m) with n = −4m; `d` = −4k, `L[d:3:d]` reads the current series at
  m − k, m − 2k, … (the stop `3` keeps the dummies out), and the weight
  `L[n-d-3]` is the next series at k − 1 in every pass, raised to `**0` for
  the partitions.
- **The print.** `L[-8]` is F₄(m − 1) = a(m) after round m; before the first
  round it is the first dummy, the conventional a(0) = 1.

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n.
- The whole b-file (201 terms) prints in about 0.1 s; the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 117 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001385), CC BY-SA 4.0.
