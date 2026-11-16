# A001862

> Number of forests of least height with n nodes.
> — [OEIS A001862](https://oeis.org/A001862)

Offset 0: 1, 1, 2, 7, 26, 111, 562, 3151, 19252, 128449, 925226, 7125009, …

### Python 3 — 106 bytes

```python
from math import*
a=[n:=1]
while[print(a[-1])]:a+=sum(comb(n-1,k)*(k+(k!=1))*a[~k]for k in range(n)),;n+=1
```

**How it works**

- **Definition.** Riordan (1968) counts forests of least height: every tree
  of the forest is a star, so a(n) counts the spanning forests of the
  complete graph on n labeled nodes whose components are stars. A star on
  k ≥ 3 nodes is fixed by its center (k ways), while one node or two joined
  nodes form one star each, which gives the e.g.f. exp(x·eˣ − x²/2) on the
  OEIS page.
- **Recurrence.** Node n lies in a star of some size k + 1 (k = 0…n−1):
  choose its k companions in C(n−1, k) ways, the star in w(k + 1) ways,
  w = 1, 1, 3, 4, 5, …, and any forest on the remaining n − 1 − k nodes:
  a(n) = Σ C(n−1, k)·w(k + 1)·a(n−1−k). This is the exponential formula
  behind the e.g.f.
- **Golf.** w(k + 1) = k + 1 except w(2) = 1 is `k+(k!=1)`. The list holds
  a(0)…a(n−1), so a(n−1−k) is `a[~k]`; `a=[n:=1]` starts both.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 106 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001862), CC BY-SA 4.0.
