# A001376

> Relational systems on n nodes.
> — [OEIS A001376](https://oeis.org/A001376)

Offset 1: 4, 32896, 3002399885885440, 14178431955039103827204744901417762816, …

Here a structure gives each ordered triple (x, y, z) of nodes one of four
values (two ternary relations), counted up to relabelling the nodes: the
entry's formula a(n) = Σ fix/(1^s₁·s₁!·2^s₂·s₂!·…) with
fix = 4^Σ ijk·sᵢsⱼsₖ/lcm(i, j, k) (Oberschelp).

### Python 3 — 152 bytes

```python
f=lambda r,*L:r and sum(f(k,*L,r-k)for k in range(r))//r or 4**(sum(sum(l*(j%l<1)for l in L)**3for j in range(M))//M)
n=M=1
while[print(f(n))]:n+=1;M*=n
```

**How it works**

- **Burnside.** a(n) = (1/n!) Σ_π 4^c(π), where c(π) is the number of cycles
  of π on the n³ triples: a structure fixed by π is constant on each cycle.
- **Cycles on triples, by Burnside again.** The cyclic group ⟨π⟩ acts on the
  triples, and πʲ fixes a triple when it fixes all three entries, so
  c(π) = (1/M) Σ_{j<M} fix(πʲ)³ for any multiple M of the order of π. A point
  on a cycle of length l is fixed by πʲ exactly when l | j, so
  fix(πʲ) = Σ_{l | j} l over the cycle lengths: `sum(l*(j%l<1)for l in L)`.
  `M` = n! is a multiple of every cycle length, and `M*=n` keeps it equal to
  n! as n grows. This replaces the lcm sum of the entry's formula and needs
  no import.
- **The sum over permutations.** `f(r,*L)` averages over the permutations of
  r further points given the cycle lengths `L` so far: for each length
  r − k of the cycle through a fixed new point, (r − 1)! of the r!
  permutations, then the remaining k points. At r = 0 it returns the weight
  4^c of the permutation with cycle lengths `L`. `//r` is exact at every
  level: each partial sum counts orbits of S_r on structures fixed by a
  permutation of the other points (de Bruijn's form of Burnside's lemma, as
  on [A000273](../../A000xxx/A000273/)).
- `r and … or …` is safe because every partial sum is positive.

**Notes**

- Exact for every n.
- The recursion visits all 2ⁿ⁻¹ compositions of n and averages over n! values
  of j at each leaf, so it slows down fast, but the b-file has only 6 terms
  (up to a(6), 128 digits) and they print in a fraction of a second; the bar
  is the whole b-file in 60 s.
- The lcm form, `4**sum(a*b*c//lcm(a,b,c)for a in L for b in L for c in L)`
  with `from math import*`, is 163 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 152 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001376), CC BY-SA 4.0.
