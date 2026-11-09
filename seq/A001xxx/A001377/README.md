# A001377

> Number of relations with 4 arguments on n nodes.
> — [OEIS A001377](https://oeis.org/A001377)

Offset 1: 2, 32896, 402975273205975947935744, …

A 4-ary relation is a set of ordered 4-tuples of nodes, so a function from
the n⁴ tuples to {0, 1}; they are counted up to relabelling the nodes.

### Python 3 — 152 bytes

```python
f=lambda r,*L:r and sum(f(k,*L,r-k)for k in range(r))//r or 2**(sum(sum(l*(j%l<1)for l in L)**4for j in range(M))//M)
n=M=1
while[print(f(n))]:n+=1;M*=n
```

The program of [A001376](../A001376/) (ternary, four values) with tuples of
length 4 and two values.

**How it works**

- **Burnside.** a(n) = (1/n!) Σ_π 2^c(π), where c(π) is the number of cycles
  of π on the n⁴ tuples: a relation fixed by π is a union of cycles.
- **Cycles on tuples, by Burnside again.** πʲ fixes a tuple when it fixes all
  four entries, so c(π) = (1/M) Σ_{j<M} fix(πʲ)⁴ for any multiple M of the
  order of π, where fix(πʲ) = Σ_{l | j} l over the cycle lengths l of π
  (`sum(l*(j%l<1)for l in L)`). `M` = n! is a multiple of every cycle length;
  `M*=n` keeps it equal to n!. The usual form
  c(π) = Σ abcd/lcm(a, b, c, d) over 4-tuples of cycles (the entry's Python
  program) gives the same number.
- **The sum over permutations.** `f(r,*L)` averages over the permutations of
  r further points given the cycle lengths `L` so far: for each length
  r − k of the cycle through a fixed new point, (r − 1)! of the r!
  permutations, then the remaining k points. At r = 0 it returns 2^c of the
  permutation with cycle lengths `L`. `//r` is exact at every level: each
  partial sum counts orbits of S_r on relations fixed by a permutation of the
  other points (de Bruijn's form of Burnside's lemma, as on
  [A000273](../../A000xxx/A000273/)).
- `r and … or …` is safe because every partial sum is positive.

**Notes**

- Exact for every n.
- 2ⁿ⁻¹ compositions times n! values of j, so the time grows quickly, but
  a(7) (720 digits) arrives in about 0.4 s here. The b-file has 7 terms (up to
  a(7)); the bar is the whole b-file in 60 s.
- Four nested loops with `lcm` and `from math import*` are 26 bytes longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 152 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001377), CC BY-SA 4.0.
