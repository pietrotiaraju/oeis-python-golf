# A001375

> Relational systems on n nodes.
> — [OEIS A001375](https://oeis.org/A001375)

Offset 1: 8, 2080, 22386176, 11728394650624, 314824619911446167552, …

Here a structure gives each ordered pair (x, y) of nodes, loops included, one
of eight values (three binary relations), counted up to relabelling the
nodes: the entry's formula a(n) = Σ fix/(1^s₁·s₁!·2^s₂·s₂!·…) over the cycle
types, with fix = 8^Σ_{i,j} gcd(i, j)·sᵢsⱼ (Oberschelp).

### Python 3 — 142 bytes

```python
import math
f=lambda r,*L:r and sum(f(k,*L,r-k)for k in range(r))//r or 8**sum(math.gcd(a,b)for a in L for b in L)
n=1
while[print(f(n))]:n+=1
```

**How it works**

- **Burnside.** a(n) = (1/n!) Σ_π 8^c(π), where c(π) is the number of cycles
  of π on the n² ordered pairs: a structure fixed by π is constant on each
  cycle. Pairs (x, y) with x on a cycle of length a and y on one of length b
  make ab pairs in orbits of length lcm(a, b), so gcd(a, b) cycles, and
  c(π) = Σ gcd(a, b) over all ordered pairs (a, b) of cycles of π, a cycle
  paired with itself included (gcd(a, a) = a). This is the exponent of the
  entry's formula, and `8**sum(math.gcd(a,b)for a in L for b in L)` computes
  it for the cycle lengths `L` of one permutation.
- **The sum over permutations.** `f(r,*L)` averages the weight over the
  permutations of r further points, given the cycle lengths `L` so far. For
  each k = 0 … r − 1, exactly (r − 1)! of the r! permutations put a fixed new
  point on a cycle of length r − k, which leaves k points: so the average is
  (1/r)·Σₖ f(k, L, r − k). At r = 0 the permutation is complete and `f`
  returns its weight. f(n) with no cycles yet is therefore the Burnside
  average, a(n).
- `//r` is exact at every level: each partial sum counts orbits of S_r on the
  structures fixed by a permutation of the other points (de Bruijn's form of
  Burnside's lemma, as on [A000273](../../A000xxx/A000273/)).
- `r and … or …` is safe because every partial sum is positive.

**Notes**

- Exact for every n; nothing is stored, the program only uses the definition
  through Burnside's lemma.
- The recursion visits all 2ⁿ⁻¹ compositions of n, so the time doubles with
  every term; the b-file has only 8 terms (up to a(8), 54 digits), which print
  at once, and the bar is the whole b-file in 60 s. The program goes on past
  the b-file.
- With so few terms required, a table of them would be shorter than the
  program, so this record needed a review.
- The cached version with incremental weights of [A000595](../../A000xxx/A000595/)
  (`<<3*k+6*sum(…)`) is 173 bytes; averaging fix(πʲ)² over j as on
  [A001376](../A001376/) is 152.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 142 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001375), CC BY-SA 4.0.
