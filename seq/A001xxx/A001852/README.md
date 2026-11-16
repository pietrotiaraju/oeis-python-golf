# A001852

> Total diameter of labeled trees with n nodes.
> — [OEIS A001852](https://oeis.org/A001852)

Offset 1: 0, 1, 6, 44, 430, 5322, 79184, 1381144, 27730602, 630422390, …

### Python 3 — 222 bytes

```python
from math import*
T=[P:=[0,1]];s=v=2;N=1
while[print(N*v-s+v//2-P[-1])]:
 N+=1;T+=P[:],;P=N*[0];s=0
 for L in T:g=[comb(N,k)*P[k]*L[-k]for k in range(N)];L+=sum(map(int.__mul__,g,range(N)))//~-N,;s+=(v:=2*L[-1]-sum(g));P=L
```

**How it works**

- **Rooted trees by height.** Let r_h(m) count rooted trees on m labeled
  nodes of height at most h. Deleting the root leaves a set of rooted trees
  of height at most h − 1, so with exponential generating functions
  R_h = x·exp(R_{h−1}), R_{−1} = 0. Then x·R_h′ = R_h + x·R_{h−1}′·R_h, which
  in coefficients is (m − 1)·r_h(m) = Σ_k C(m, k)·k·r_{h−1}(k)·r_h(m − k).
  `T` keeps one list per level h = 0, 1, …, indexed by the node count; each
  pass appends the next coefficient to every level, bottom up so that `P`
  is the level below (the zero list `N*[0]` under level 0), and adds a
  copy of the top level, which equals R (r(m) = mᵐ⁻¹) up to the current
  size N.
- **Diameter at most 2h.** A tree has diameter at most 2h exactly when some
  vertex has eccentricity at most h. Those vertices form a subtree S, and an
  edge lies in S exactly when the two rooted trees it separates both have
  height at most h − 1. Summing |vertices of S| − |edges of S| = 1 over all
  labeled trees with S nonempty gives c_{2h} = R_h − R_{h−1}²/2 (products
  of exponential generating functions; the edge's two sides are an ordered
  pair, hence the 1/2).
- **Diameter 2h + 1.** Such a tree has a central edge joining two rooted
  trees of height exactly h: (R_h − R_{h−1})²/2 of them.
- **Total diameter.** a(N) = Σ_{d≥0} (t − c_d) at xᴺ/N!, where
  t = R − R²/2 counts the free trees. Expanding,
  c_{2h} + c_{2h+1} = V_h + (R_h² − R_{h−1}²)/2 with V_h = 2R_h − R_h·R_{h−1};
  the second part telescopes over h = 0…N−1 to R²/2 = R − t, so
  a(N) = Σ_h (2t − V_h) + t − r(N). The top level gives V = 2t, since
  R_{N−2} agrees with R below xᴺ.
- **In the code.** Before a level's new term, `g` lists
  g_k = C(N, k)·r_{h−1}(k)·r_h(N − k). The recurrence makes the new term
  Σ k·g_k/(N − 1), and the labeled product R_h·R_{h−1} at xᴺ is Σ g_k
  (C(N, k) = C(N, N − k)), so `s` adds V_h = 2r_h(N) − Σ g_k and `v` keeps
  the last one, 2t. With N levels the header prints N·v − s + v/2 − r(N).

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 18 terms (n = 1 to 18), which take well under a second;
  the bar is the whole b-file in 60 s. They fit in a table shorter than
  the program, so this program needs a review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 222 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001852), CC BY-SA 4.0.
