# A000298

> Number of partitions into non-integral powers.
> — [OEIS A000298](https://oeis.org/A000298)

Offset 1: 1, 4, 12, 30, 70, 159, 339, 706, 1436, 2853, 5551, 10622, 19975, …

As R. J. Mathar reads it on the OEIS page, a(n) counts the nonempty sets of
distinct positive integers x₁ < x₂ < ⋯ with √x₁ + √x₂ + ⋯ ≤ n. For n = 2
these are {1}, {2}, {3} and {4}; {1, 2} already weighs 2.414….

### Python 3 — 177 bytes

```python
import math
f=lambda b,i:b<W[i]or f(b-W[i],i+1)+f(b,i+1)
n=M=1
while 1:M*=2;a,b=[f(n*M,0)for e in(0,1)if[W:=[math.isqrt(x*M*M-e)+e for x in range(1,4*n*n)]]];n+=a==b!=print(a-1)
```

**How it works**

- The [A000135](../A000135/) program with square roots in place of
  x^(2/3). Floats cannot decide whether a sum of square roots is ≤ n, so
  every x gets two integer weights at scale M (a power of 2):
  ⌊√x·M⌋ = `isqrt(x*M*M)` for e = 0 and ⌈√x·M⌉ = `isqrt(x*M*M-1)+1` for
  e = 1 (right whether xM² is a square or not).
- Let U count the sets whose floor weights sum to at most n·M and L those
  whose ceiling weights do, both including the empty set. Every set with
  Σ√x ≤ n is in U, and every set in L has Σ√x ≤ n, so L ≤ a(n) + 1 ≤ U.
  When L = U, both equal a(n) + 1: `n+=a==b!=print(a-1)` prints and moves
  on only then, and otherwise M doubles and the same n is tried again.
- `f(b,i)` counts the subsets of `W[i:]` with sum ≤ b by taking or skipping
  `W[i]`; the weights never decrease, so `W[i]>b` leaves only the empty
  set. x runs to 4n² − 1: past (n + 1)² for n ≥ 2, and for n = 1 the
  weight ⌊√3·M⌋ > M once M ≥ 2, so the list always ends above the budget
  and `f` never runs off its end.
- **It never stalls.** A sum √x₁ + ⋯ + √xₖ equal to the integer n forces
  every xᵢ to be a perfect square, because the square roots of distinct
  squarefree integers are linearly independent over ℚ (Besicovitch, 1940)
  and all the coefficients here are positive. For such sets both weights
  are exact. Every other set has Σ√x ≠ n, and once M is large enough both
  counts sort it the same way. M doubles every pass and is never reset.

**Notes**

- Exact integer arithmetic; correctness rests only on the bracket argument
  and Besicovitch's theorem above, nothing conjectural.
- `f` visits every counted set, so a term costs a few times a(n) calls:
  here a(22) prints after about 12 s and a(26) after about 56 s, 26 terms
  in 60 s; the bar is 22 terms in 60 s. The b-file is synthesized from the
  entry's data (37 terms, up to a(37) ≈ 5·10⁹).
- The skip branch of `f` goes one level deeper per weight under the
  budget, about n² levels, so near n = 31 it passes CPython's default
  recursion limit of 1000 frames; the program is far slower than that point
  anyway (a(31) ≈ 3·10⁸ sets).
- `import math` with `math.isqrt` is 1 byte under `from math import*` with
  `isqrt`, and A000135's integer Newton lambda for the root is longer than
  either.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 177 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000298), CC BY-SA 4.0.
