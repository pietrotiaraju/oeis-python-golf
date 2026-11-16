# A001828

> Related to graded partially ordered sets.
> — [OEIS A001828](https://oeis.org/A001828)

Offset 0: 1, 5, 33, 287, 3309, 50975, 1058493, 29885567, 1156711869, 61815727295, …

### Python 3 — 131 bytes

```python
from math import*
n=0
while[print(sum(comb(n,t)*comb(t,q)*(2**q+2**t+2**(t-q))**(n-t)for t in range(n+1)for q in range(t+1)))]:n+=1
```

**How it works**

- **The count.** Klarner's c(5, n): put n labeled points on 5 numbered
  levels and join points of neighbouring levels by any set of edges, so
  a(n) = Σ n!/(p₁!⋯p₅!)·2^(p₁p₂+p₂p₃+p₃p₄+p₄p₅) over compositions of n
  (Sean A. Irvine's formula on the OEIS page). Each choice is a labeled
  poset (the edges are its cover relations) with a rank function into 5
  levels.
- **Summing out levels 1, 3 and 5.** They touch only levels 2 and 4, which
  hold q and s points. In the e.g.f., level 1 gives exp(2^q·x), level 3
  exp(2^(q+s)·x) and level 5 exp(2^s·x). With t = q + s,
  a(n) = Σₜ Σ_q C(n, t)·C(t, q)·(2^q + 2^t + 2^(t−q))^(n−t), over
  0 ≤ q ≤ t ≤ n: each of the n − t other points picks level 1, 3 or 5
  together with its edges to the kept levels.
- **The program.** One generator over the pairs (t, q), as in
  [A001827](../A001827/) (4 levels) with one more power of 2. Six and seven
  levels ([A001829](../A001829/), [A001830](../A001830/)) would need three
  kept levels, so they use a cached recursion over the levels instead.

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(n)
  passes the 4300-digit int-to-str limit near n = 237.
- The b-file has 113 terms (n = 0 to 112); the bar is the whole b-file in
  60 s, which takes about two seconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 131 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001828), CC BY-SA 4.0.
