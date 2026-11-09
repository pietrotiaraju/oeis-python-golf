# A001258

> Number of labeled n-node trees with unlabeled end-points.
> — [OEIS A001258](https://oeis.org/A001258)

Offset 2: 1, 1, 2, 6, 25, 135, 892, 6937, 61886, 621956, 6946471, 85302935, 1141820808, 16540534553, 257745010762, …

### Python 3 — 165 bytes

```python
from math import*
n=2
while[print(1+sum(comb(m,b)*comb(n+b+~m,m-1)*sum((-1)**j*comb(b,j)*(b-j)**(m-2)for j in range(m))for m in range(2,n-1)for b in range(m)))]:n+=1
```

**How it works**

- A tree with unlabeled end-points has its m internal nodes labeled
  1…m and k = n − m unlabeled leaves. Removing the leaves leaves a
  labeled tree T on the internal nodes when m ≥ 2. Putting the leaves
  back means choosing how many hang on each internal node: c_v ≥ 0 with
  Σ c_v = k. Each leaf of T needs c_v ≥ 1, since otherwise it would be an
  end-point itself. If T has i leaves, there are C(k − i + m − 1, m − 1)
  ways to do this.
- Labeled trees on m nodes with i leaves are C(m, i)·Surj(m − 2, m − i):
  the leaves are the labels that are missing from the Prüfer code. Here
  Surj(a, b) = Σ_j (−1)ʲ C(b, j)(b − j)ᵃ counts the surjections from a
  set of size a onto a set of size b.
- With b = m − i this gives a(n) = 1 + Σ_{m=2}^{n−2} Σ_b C(m, b)·
  C(n + b − m − 1, m − 1)·Surj(m − 2, b). The 1 is the star with one
  internal node, and also the single edge at n = 2. Terms with i < 2 have
  Surj = 0, so `b` and `j` can both run over `range(m)`. The term b = 0,
  m = 2 uses 0⁰ = 1. This is the same sum as the Maple program in the
  OEIS entry.

**Notes**

- A term costs about n³/6 steps. The whole b-file (99 terms) prints in
  about 7 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 165 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001258), CC BY-SA 4.0.
