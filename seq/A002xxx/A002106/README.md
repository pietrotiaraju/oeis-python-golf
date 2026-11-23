# A002106

> Number of transitive permutation groups of degree n.
> — [OEIS A002106](https://oeis.org/A002106)

Offset 1: 1, 1, 2, 5, 5, 16, 7, 50, 34, 45, 8, 301, 9, 63, 104, 1954, 10, 983, …

### Python 3 — 642 bytes

```python
from itertools import*
n=0
while n:=n+1:
 P=[*permutations(range(n))];c=lambda s,x:tuple(s.index(x[j])for j in s);R=[(frozenset(P[:1]),[])];S={0}
 for H,G in R:
  N=[s for s in P if all(c(s,x)in H for x in G)];V={*H}
  for g in P:
   if g in V:continue
   V|={tuple(h[i]for i in y)for y in{c(s,g)for s in N}for h in H};F=K={*H};L=G+[g]
   while F and n**(n>4)*len(K)<=len(P):F={tuple(x[i]for i in s)for x in F for s in L}-K;K|=F
   if not F and(K:=frozenset(K))not in S:
    R+=(K,L),;Q=[K]
    for X in Q:Q+=(Z:={frozenset(c(s,x)for x in X)for s in[(*range(1,n),0),*P[1:2]]}-S);S|=Z
 print(sum(len({x[0]for x in K})==n for K,G in R)+2*(n>4))
```

**How it works**

- The groups are counted up to conjugacy in S_n (permutation isomorphism),
  which is how the data counts them: a(4) = 5 is C4, V4, D4, A4 and S4. So
  a(n) is the number of conjugacy classes of subgroups of S_n whose orbit of 0
  is all of {0, ..., n−1}. A permutation is a tuple x with i ↦ x[i], and
  `c(s,x)` is the conjugate s⁻¹xs.
- The program finds one subgroup from each conjugacy class of subgroups of
  S_n. `R` holds the representatives found so far, each with a list of
  generators, and `S` holds every conjugate of each of them, so a subgroup is
  new exactly when it is not in `S`. The list starts with the trivial group,
  and each representative H in turn is extended by every g ∉ H: K = ⟨H, g⟩ is
  the closure of H under right multiplication by the generators of H and g.
  When K is new it joins `R`, and its whole class goes into `S` by a search
  under conjugation by the n-cycle (1, 2, ..., n−1, 0) and the transposition
  `P[1]` of the last two points, which generate S_n.
- Every class is reached. A subgroup K ≠ 1 has a maximal subgroup M, and by
  induction on the order M is conjugate to a representative H; conjugating K
  the same way gives K′ ⊃ H with H maximal in K′, so K′ = ⟨H, g⟩ for any
  g ∈ K′ outside H.
- Some g are skipped, but only when ⟨H, g⟩ is conjugate to a subgroup already
  formed. After g is used, `V` gets h·t⁻¹gt for every h ∈ H and every t in
  the normalizer N of H (t normalizes H exactly when it conjugates the
  generators of H into H). For such an element y, ⟨H, y⟩ = t⁻¹⟨H, g⟩t, so
  nothing is lost.
- For n ≥ 5 a closure stops as soon as it has more than (n−1)! elements,
  because then it is A_n or S_n. A subgroup of index k < n gives, by its
  action on its k cosets, a homomorphism S_n → S_k whose kernel lies in the
  subgroup. Since k! < n!, the kernel is a nontrivial normal subgroup of S_n,
  so it is A_n or S_n. Neither group is needed to build any other subgroup, so
  they are not stored and are added at the end as `2*(n>4)`, both transitive.
  For n ≤ 4 the bound is false (D4 has index 3 in S4), and there is no cut.

**Notes**

- The 7th term arrives after about 6 reference seconds, and the 8th is out of
  reach: S_8 has 296 classes of subgroups and the normalizer scans over its
  40320 elements alone take minutes. So the bar is 7 terms. While the program
  works on n = 8 it uses about 0.75 GB.
- The b-file is the OEIS one (synthesized from the entry, 47 terms).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 642 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002106), CC BY-SA 4.0.
