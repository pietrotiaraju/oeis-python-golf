# A001851

> Total diameter of unlabeled trees with n nodes.
> — [OEIS A001851](https://oeis.org/A001851)

Offset 1: 0, 1, 2, 5, 9, 21, 44, 103, 232, 571, 1368, 3441, 8653, 22263, …

### Python 3 — 216 bytes

```python
T=[P:=[n:=0,1]];s=v=2
while[print(-~-n*v-s+v//2-P[-1])]:
 n-=1;T+=P[:],;P=-n*[0,0];s=0
 for L in T:L+=sum(d*P[-d]*sum(L[d::d])for d in range(n,0))//n,;s+=(v:=2*L[-1]-sum(map(int.__mul__,L,P[::-1]))+n%2*L[1-n>>1]);P=L
```

**How it works**

- **Rooted trees by height.** Let r_h(m) count rooted trees on m unlabeled
  nodes of height at most h, R_h(x) = Σ r_h(m)xᵐ. The subtrees of the root
  form a multiset of trees of height at most h − 1, so
  R_h(x) = x·exp(Σ_k R_{h−1}(xᵏ)/k), R_{−1} = 0 (Riordan 1960). As in
  [A001853](../A001853/), `T` keeps one list per level, in the layout of
  [A000081](../../A000xxx/A000081/) (`n` counts down, `P` is the level
  below, `-n*[0,0]` the zero list under level 0), and every pass appends
  the next coefficient to each level and adds a copy of the top level,
  which equals R = A000081 up to the current size N.
- **Diameter at most 2h.** A tree has diameter at most 2h exactly when some
  vertex has eccentricity at most h. Those vertices form a subtree S, and an
  edge uv lies in S exactly when the two rooted trees it separates both have
  height at most h − 1. Otter's count for a tree acted on by its
  automorphism group (vertex orbits − edge orbits + flipped edges = 1),
  applied to S, gives the number of such trees:
  c_{2h} = R_h − SET₂(R_{h−1}), with SET₂(F) = (F(x)² − F(x²))/2.
- **Diameter 2h + 1.** Such a tree has a central edge joining two rooted
  trees of height exactly h, so there are MSET₂(R_h − R_{h−1}) of them,
  MSET₂(F) = (F(x)² + F(x²))/2.
- **Total diameter.** a(N) = Σ_{d≥0} (t − c_d), where t = R − SET₂(R) is
  the number of free trees (Otter) and c_d counts trees of diameter at most
  d, all at x^N. Expanding, c_{2h} + c_{2h+1} = V_h + SET₂(R_h) −
  SET₂(R_{h−1}) with V_h = 2R_h − R_h·R_{h−1} + R_h(x²); the second part
  telescopes over h = 0…N−1 to SET₂(R) = R − t, so
  a(N) = Σ_h (2t − V_h) + t − r(N). The top level gives V = 2t, since
  R_{N−2} agrees with R below x^N.
- **In the code.** After a level gets its new term, `s` adds
  V_h = 2r_h(N) − Σ_k r_h(k)·r_{h−1}(N−k) + [N even]·r_h(N/2) (the map
  multiplies the list by the reversed level below, and `L[1-n>>1]` is
  r_h(N/2)), and `v` keeps the last one, 2t. With N = 1 − n levels the
  header prints N·v − s + v/2 − r(N).

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 30 terms (n = 1 to 30), which take well under a second;
  the bar is the whole b-file in 60 s. They fit in a table shorter than
  the program, so this program needs a review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 216 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001851), CC BY-SA 4.0.
