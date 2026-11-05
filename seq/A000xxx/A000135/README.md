# A000135

> Number of partitions into non-integral powers.
> — [OEIS A000135](https://oeis.org/A000135)

Offset 1: 1, 2, 6, 13, 24, 42, 73, 125, 204, 324, 511, 801, …

As R. J. Mathar reads it on the OEIS page, a(n) counts the nonempty sets of
distinct positive integers x₁ < x₂ < ⋯ with x₁^(2/3) + x₂^(2/3) + ⋯ ≤ n.
For n = 3 these are {1}, {2}, {3}, {4}, {5} and {1, 2}.

### Python 3 — 211 bytes

```python
c=lambda v,t:v<t**3and c(v,(2*t+v//t//t)//3)or t
f=lambda b,i:b<W[i]or f(b-W[i],i+1)+f(b,i+1)
n=M=1
while 1:M*=2;a,b=[f(n*M,0)for e in(0,1)if[W:=[c(t*t*M-e,t)+e for t in range(M,3*n*n*M,M)]]];n+=a==b!=print(a-1)
```

**How it works**

- Floats cannot decide whether a sum of cube roots is ≤ n, so the program
  scales by M (a power of 2) and gives every x two integer weights,
  ⌊x^(2/3)·M⌋ and ⌈x^(2/3)·M⌉. Let U count the sets whose floor weights sum
  to at most n·M and L the sets whose ceiling weights do (both including the
  empty set). Every set with x₁^(2/3) + ⋯ ≤ n is in U, and every set in L
  has x₁^(2/3) + ⋯ ≤ n, so L ≤ a(n) + 1 ≤ U. When L = U, both equal
  a(n) + 1.
- `c(v,t)` is integer Newton's method for ⌊∛v⌋ from a start t ≥ ∛v: while
  t³ > v it steps to ⌊(2t + ⌊v/t²⌋)/3⌋. By AM–GM a step never goes below
  ⌊∛v⌋, and it strictly decreases t until t³ ≤ v, so it stops exactly at
  ⌊∛v⌋.
- `t` runs over x·M for x = 1, …, 3n² − 1, so `t*t*M` is x²M³ and
  `c(t*t*M,t)` is ⌊x^(2/3)·M⌋, with t itself as the start. For e = 1,
  `c(v-1,t)+1` is ⌈∛v⌉, whether v is a cube or not. Weights grow with x, and
  x = 3n² − 1 already weighs more than n·M once M ≥ 2, so the list is long
  enough.
- `f(b,i)` counts the subsets of `W[i:]` with sum ≤ b by including or
  skipping `W[i]`. Since the weights grow, `W[i]>b` means only the empty set
  is left, and `b<W[i]or` returns `True`, which counts as 1.
- Each pass doubles M and works out U and L as `a` and `b`. In
  `n+=a==b!=print(a-1)`, `print` runs only when `a==b` (the chain stops at
  the first false comparison); it returns `None`, so `b!=None` is `True` and
  n moves on. Otherwise the next pass tries the same n with twice the
  precision.

**Why it is exact, and why it does not stall**

- A printed term rests only on L = U, computed in integers, so it is never
  wrong.
- A pass fails only if some set has its floor sum ≤ n·M < its ceiling sum,
  so its x₁^(2/3) + ⋯ is within k/M of n (k = the size of the set) without
  the ceiling sum fitting. A set whose sum is exactly n is never such a set,
  as long as its sum being n forces every x to be a cube, since then all its
  weights are exact. That holds by Besicovitch's theorem (A. S. Besicovitch,
  *On the linear independence of fractional powers of integers*, J. London
  Math. Soc. 15 (1940), 3–6): cube roots of distinct cube-free integers are
  linearly independent over ℚ. A non-cube x has x^(2/3) = r·m^(1/3) with r
  rational and m > 1 cube-free, and the coefficients only add up, so any sum
  with a non-cube term is irrational. Every other set misses n by some
  positive amount, only finitely many sets are in play for a given n, and so
  some M makes the pass succeed.
- In practice only four passes fail on the b-file: two at n = 2 and two at
  n = 5. M is 2⁴² by n = 38.

**Notes**

- Each pass enumerates every set twice, so the time follows a(n), which
  roughly multiplies by 1.33 per term near n = 38. The program prints the 38
  terms of the b-file in about 20 s and 41 in a minute. The bar is the whole
  b-file (38 terms) in 60 s.
- The OEIS page links Sean A. Irvine's tentative values of the first 55
  terms, computed with double-precision floats. An ungolfed exact version of
  this method confirms them up to n = 47.
- `f` recurses about n^1.5 levels deep, so the default recursion limit of
  1000 stops the program near n = 99, far beyond what it reaches in any
  reasonable time.
- `v<t**3and` saves a byte over `t**3>v and` at the price of a
  `SyntaxWarning`.
- Discarded variants: `try:a,={…};print(a-1);n+=1` with `except:M*=2`
  (unpacking a two-element set raises) came to 221 bytes. One enumeration
  carrying both budgets and raising `ZeroDivisionError` through `1//(d>=0)`
  at an ambiguous set came to 247. Passing slices `W[1:]` instead of an
  index saves a few bytes but copies the list at every call and manages only
  36 terms in two minutes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 211 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000135), CC BY-SA 4.0.
