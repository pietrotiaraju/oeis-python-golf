# A000019

> Number of primitive permutation groups of degree n.
> — [OEIS A000019](https://oeis.org/A000019)

Offset 1: 1, 1, 2, 2, 5, 4, 7, 7, 11, 9, 8, 6, 9, 4, 6, 22, 10, 4, 8, 4, …

Groups are counted up to conjugacy in Sₙ.

### Python 3 — 469 bytes

```python
from itertools import*
c=lambda K:K<(T:={tuple(a[i]for i in b)for a in K for b in K})and c(T)or K
n=1
while 1:
 P=[*permutations(R:=range(n))];L=[{P[0]}]
 for H in L:
  D={*H}
  for g in P:
   if{g}-D:K=c(H|{g});D|={tuple(a[i]for i in g)for a in H};L+=[K][K in L:]
 print(sum({tuple(s[k[s.index(i)]]for i in R)for k in K}==K for K in L if n<=len(K)*all(any(len({*B,*(k[x]for x in B)})%m for k in K)for m in range(2,n)for B in combinations(R,m))for s in P)//len(P));n+=1
```

**How it works**

- **Every subgroup of Sₙ.** `L` starts with the trivial group and, for each
  group H in it, adds ⟨H, g⟩ for every permutation g. Each subgroup is
  reached this way by adding its generators one at a time.
  `L+=[K][K in L:]` appends K only when it is new.
- **Closure.** `c` multiplies the set by itself until it stops growing. In a
  finite group that is enough: inverses are powers.
- **Skipping work.** ⟨H, hg⟩ = ⟨H, g⟩ for h in H, so after using g the
  program marks its whole right coset Hg in `D` and skips it. (Skipping
  every g inside an overgroup already found would be wrong: g ∈ ⟨H, g′⟩ does
  not make ⟨H, g⟩ that big.)
- **Primitive.** A group is primitive when it is transitive and has no block
  B with 2 ≤ |B| < n, a set that every element maps onto itself or off
  itself. That happens exactly when |B ∪ k(B)| is |B| or 2|B|, so the test is
  `len(…)%m`. For n ≥ 3 an intransitive group always has such a block (one of
  its orbits, or any pair for the trivial group). Only n = 2 needs the
  transitivity test: `n<=len(K)` throws out the trivial group there, and a
  transitive group always has at least n elements.
- **Up to conjugacy.** The number of conjugacy classes is the sum of
  |N(K)| / n! over the primitive subgroups K (orbit–stabilizer). The program
  counts the pairs (K, s) with s K s⁻¹ = K and divides by n!.

**Notes**

- The program prints a(1)…a(5) in about a minute; the bar is 5 terms in
  120 s. a(6) means all 1455 subgroups of S₆ and would take hours. The b-file
  (up to n = 4095) comes from the library of primitive groups, which no
  enumeration can match.
- Taking only 2-generated subgroups would be much faster but wrong in
  general: an affine primitive group V⋊H needs at least as many generators as
  H. For example, the extraspecial group 2^(1+4) acts irreducibly on
  𝔽₃⁴ and needs 4, which gives a primitive group of degree 81 that needs at
  least 4 generators.
- Without the coset skip the program is 427 bytes, but it does not reach
  a(5) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 469 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000019), CC BY-SA 4.0.
