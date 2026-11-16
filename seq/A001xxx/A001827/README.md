# A001827

> Related to graded partially ordered sets.
> — [OEIS A001827](https://oeis.org/A001827)

Offset 0: 1, 4, 22, 166, 1726, 24814, 494902, 13729846, 531077086, 28697950174, …

### Python 3 — 122 bytes

```python
from math import*
n=0
while[print(sum(comb(n,t)*comb(t,q)*(2**q+2**t)**(n-t)for t in range(n+1)for q in range(t+1)))]:n+=1
```

**How it works**

- **The count.** Klarner's c(4, n): put n labeled points on 4 numbered
  levels, p, q, r, s points on levels 1 to 4, and join points of
  neighbouring levels by any set of edges. That is Sean A. Irvine's
  formula on the OEIS page, a(n) = Σ n!/(p!q!r!s!)·2^(pq+qr+rs) over
  p + q + r + s = n. Each choice is a labeled poset (the edges are its
  cover relations) together with a rank function into 4 levels.
- **Summing out levels 1 and 3.** In the e.g.f. Σ x^(p+q+r+s)/(p!q!r!s!)
  ·2^(pq+qr+rs), level 1 meets only level 2 and level 3 meets only levels
  2 and 4, so Σₚ xᵖ/p!·2^(pq) = exp(2^q·x) and
  Σᵣ xʳ/r!·2^(r(q+s)) = exp(2^(q+s)·x). With t = q + s that leaves
  a(n) = Σₜ Σ_q C(n, t)·C(t, q)·(2^q + 2^t)^(n−t), over 0 ≤ q ≤ t ≤ n:
  the n − t points off levels 2 and 4 each pick level 1 (2^q ways to join
  level 2) or level 3 (2^t ways to join levels 2 and 4).
- **The program.** One generator over the pairs (t, q), O(n²) terms per
  n. Five levels ([A001828](../A001828/)) still need only two kept levels
  (2 and 4); six and seven ([A001829](../A001829/),
  [A001830](../A001830/)) would need three, so they use a cached recursion
  over the levels instead.

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(n)
  passes the 4300-digit int-to-str limit near n = 237.
- The b-file has 113 terms (n = 0 to 112); the bar is the whole b-file in
  60 s, which takes about a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 122 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001827), CC BY-SA 4.0.
