# A000083

> Number of mixed Husimi trees with n nodes; or polygonal cacti with bridges.
> — [OEIS A000083](https://oeis.org/A000083)

Offset 0: 1, 1, 1, 2, 4, 9, 23, 63, 188, 596, 1979, 6804, 24118, 87379, …

A cactus here is a connected graph in which every block is a bridge or a
polygon (a cycle of length at least 3).

### Python 3 — 262 bytes

```python
from math import*
p=sumprod;S=[1];R=S*2;t=K=[-1];print(n:=1)
while S:=[s:=p(R[1:],S[::2]),0]+S:P=p(R,S[n:]);K=[s+P>>1]+K;t+=~-n*s-p(t,S[:-1:2]),;print(sum(t[gcd(i,n)]for i in range(n))//n+P-p(R,K)>>1);n+=1;R+=sum(d*K[~d]*sum(R[-d:0:-d])for d in range(1,n))//~-n,
```

**How it works**

Let r(x) = x + x² + 3x³ + 8x⁴ + … count rooted cacti
([A000237](https://oeis.org/A000237)) and write R = 1 + r. Every power
series below is truncated at the current n.

- **Rooted cacti.** Each block at the root has a sequence of rooted cacti
  hanging off its other nodes: one for a bridge, k ≥ 2 for a polygon. Read backwards, the sequence describes the same
  block, so blocks are counted by **BIK(r) − 1**, sequences up to reversal,
  and the root carries a multiset of them: r = x · EULER(BIK(r) − 1), the
  formula on the A000237 page.
- **BIK.** With S = 1/(1 − r) (all sequences) and palindromes
  P = (1 + r) · S(x²) (the middle element, or none, then half the sequence),
  BIK(r) = (S + P)/2, counted by Burnside's lemma: a sequence and its reverse
  pair up except for palindromes.
- **Unrooted cacti.** By the dissymmetry theorem for tree-like structures,
  unrooted = rooted at a node + rooted at a block − rooted at a node in a
  block. Bracelets (cycles up to rotation and reflection) of rooted cacti
  give the block-rooted ones, since a bridge is a 2-cycle and a polygon a
  k-cycle with k ≥ 3, so A = r + DIK(r) − r · BIK(r). That is Christian
  Bower's formula on the OEIS page (B + C − B·D with A000237, A035349,
  A035350), and the DIK term supplies a(0) = 1.
- **One formula.** DIK(r) = 1 + (CIK(r) + (R²S(x²) − 1)/2)/2, where CIK
  counts necklaces. Substituting BIK and using rS = S − 1, everything
  collapses to **A = R + (CIK(r) + P − R · BIK(r))/2**.
- **Necklaces.** Let t(m) = Σ k·r(k)·S(m−k), the cycles of m nodes cut
  into blocks, with one position marked (t = x·r′·S = x·(log S)′). By
  Burnside's lemma over the n rotations, **CIK(r)ₙ = (1/n) Σ t(gcd(i, n))**
  for 0 ≤ i < n. The program gets t from n·S(n) = Σ t(k)·S(n−k) rather than
  from its definition.

**The lists**

- `S` holds S(n), 0, S(n−1), 0, …, 0, S(0): S reversed, with zeros
  in between. `S[::2]` is S reversed, and `S[n:]` is S(x²) reversed, so
  P(n) is one `sumprod` with `R`, which holds R(0), …, R(n) in order. The
  update sits in the `while` condition (a non-empty list is truthy), and
  `s` keeps S(n).
- `K` holds BIK(n), …, BIK(1) and then −1 in place of BIK(0) = 1. Then
  `p(R,K)` is R · BIK minus 2R(n), and the leading R in the formula
  disappears: the program prints (C + P − `p(R,K)`)/2.
- `t` holds t(0), t(1), …, and starts as the same list `[-1]` as `K`. The
  sentinel t(0) = −1 puts −S(n) into the `sumprod`, which starting from
  `~-n*s` = (n − 1)·S(n) makes up for. The sharing is harmless: `t` grows
  in place, while `K=[…]+K` builds a new list before `t` first changes.
- `R` gets the next rooted count from the Euler-transform recurrence with
  the two sums swapped, as in [A000055](../A000055/):
  (n−1)·r(n) = Σ d·BIK(d) · Σ_{j≥1} r(n − jd), for 1 ≤ d < n. `K[~d]` is
  BIK(d), and `R[-d:0:-d]` walks r(n−d), r(n−2d), … and stops before
  R(0) = 1.
- `>>1` halves without brackets because `+` and `-` bind tighter.
  `math.sumprod` (Python 3.12+) needs equal lengths, which the slices
  give.

**Notes**

- Exact integer arithmetic throughout. Every division is exact: S + P is
  even (non-palindromes pair up), the Burnside sum is a multiple of n, the
  Euler recurrence's sum is a multiple of n − 1, and the printed bracket is
  2·a(n).
- a(0) is printed before the loop, which starts at n = 1 so that no
  division is by zero.
- The whole b-file (a(0)…a(500)) prints in about 0.3 s, and 2000 terms in
  about 26 s. The bar is the whole b-file in 60 s. Terms grow roughly like
  4.48ⁿ (a(500) has 320 digits), so Python's 4300-digit int-to-str limit
  is only reached near n = 6600.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 262 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000083), CC BY-SA 4.0.
