# A002086

> Number of circulant tournaments on 2n+1 nodes up to Cayley isomorphism.
> — [OEIS A002086](https://oeis.org/A002086)

Offset 1: 1, 1, 2, 4, 4, 6, 16, 16, 30, 88, 94, 208, 472, 586, …

### Python 3 — 180 bytes

```python
from math import*
m=3
while[print(sum(x:=[all(gcd(h+1,m)<2for h in H)<<sum(gcd(h-1,m)for h in H)//len(H)//2for k in range(m)if 1in(H:={k**j%m for j in range(1,m)})])//len(x))]:m+=2
```

**How it works**

- **What is counted.** With m = 2n + 1, a circulant tournament on Z_m is
  given by its connection set S (x → y when y − x ∈ S), and it is a
  tournament exactly when S holds one element of each pair {u, −u},
  u ≠ 0. Cayley isomorphisms are the automorphisms x ↦ kx of Z_m
  (k a unit), which send S to kS. So a(n) is the number of orbits of the
  unit group on these sets, and Burnside's lemma gives
  a(n) = (1/φ(m)) Σ_k fix(k), as in Andrew Howroyd's PARI program in the
  entry.
- **fix(k).** kS = S means S is a union of orbits of H = ⟨k⟩ acting on
  Z_m ∖ {0} by multiplication. If some orbit is closed under negation,
  S can hold neither it nor its complement, and fix(k) = 0; otherwise
  the orbits come in pairs O, −O and S takes one of each: 2^(c/2) sets
  for c orbits.
- **Closed orbits.** −u ∈ uH means u(h + 1) ≡ 0 (mod m) for some h ∈ H;
  such a u in 1 … m − 1 exists iff gcd(h + 1, m) > 1 (take
  u = m/gcd(h + 1, m)). So fix(k) ≠ 0 iff `all(gcd(h+1,m)<2for h in H)`.
- **Counting orbits.** By Burnside again, within H, the orbits on all of
  Z_m number (1/|H|) Σ_{h∈H} gcd(h − 1, m) (u is fixed by h when
  m | u(h − 1)); that is c + 1 with the orbit {0}. When fix(k) ≠ 0, c is
  even and (c + 1)//2 = c/2 is the shift.
- **The units.** `H` is the set of k^j mod m for j = 1 … m − 1, which
  is all of ⟨k⟩ because the order of k is at most φ(m) ≤ m − 1; it
  contains 1 exactly when k is a unit, so `1in H` picks the units and
  `len(x)` is φ(m). `all(…)<<e` is 2^e or 0.

**Notes**

- Exact integer arithmetic; the Burnside sum is a multiple of φ(m), so
  the program is right for every n.
- About O(m²) work per term (`k**j%m` is shorter than `pow(k,j,m)`,
  which `from math import*` would shadow anyway). The whole b-file
  (200 terms, m up to 401) takes about 27 s here; the bar is all 200 in
  60 s.
- [A002087](https://oeis.org/A002087) (all point-symmetric tournaments up
  to isomorphism) differs from this sequence from n = 4 on.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 180 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002086), CC BY-SA 4.0.
