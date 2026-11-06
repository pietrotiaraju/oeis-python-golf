# A000234

> Partitions into non-integral powers (see Comments for precise definition).
> — [OEIS A000234](https://oeis.org/A000234)

Offset 1: 1, 3, 8, 18, 37, 72, 136, 251, 445, 770, 1312, 2202, …

As R. J. Mathar reads it on the OEIS page, a(n) counts the nonempty multisets
of positive integers x₁ ≤ x₂ ≤ ⋯ with x₁^(2/3) + x₂^(2/3) + ⋯ ≤ n. For n = 3
these are {1}, {2}, {3}, {4}, {5}, {1, 1}, {1, 2} and {1, 1, 1}. It is
[A000135](../A000135/) with repeated parts allowed.

### Python 3 — 157 bytes

```python
f=lambda b,t,s:s**3>(v:=t*t*M-1)and f(b,t,(2*s+v//s//s)//3)or n<=b<=s or f(b+~s,t,s)+f(b,t+M,s+M)
n=M=1
while 1:
 try:print(f(n*M+n,M,M)-1);n+=1
 except:M*=2
```

**How it works**

- Floats cannot decide whether a sum of cube roots is ≤ n, so every x gets
  the integer weight w(x) = ⌈x^(2/3)·M⌉ for a scale M (a power of 2). For a
  multiset with k parts, true sum T and weight sum C, this gives
  T·M ≤ C < T·M + k, and C = T·M when every part is a cube.
- So a multiset with C ≤ nM has T ≤ n, and a multiset with T ≤ n (hence
  k ≤ n, as every part weighs at least 1) has C ≤ nM + n. If no multiset
  falls in the window nM < C ≤ nM + n, the multisets with C ≤ nM + n are
  exactly those with T ≤ n, and counting them gives a(n) + 1, the empty one
  included.
- `f(b,t,s)` counts the multisets of parts ≥ x = t/M whose weights fit in
  the budget b: take one more x (`f(b+~s,t,s)`, as w(x) = s + 1) or move on
  to x + 1 (`f(b,t+M,s+M)`). Weights grow with x, so once x no longer fits
  (`b<=s`) only the empty multiset is left, and `True` counts it as 1.
- The weight: `t*t*M-1` is v = x²M³ − 1, and s ends as ⌊∛v⌋, so s + 1 is
  ⌈∛(x²M³)⌉ = w(x) whether x is a cube or not. The first branch is integer
  Newton's method: while s³ > v it steps to ⌊(2s + ⌊v/s²⌋)/3⌋, which by
  AM–GM never drops below ⌊∛v⌋ and strictly decreases s, so it stops
  exactly at ⌊∛v⌋. It needs a start above that: M for x = 1, and s + M for
  x + 1, since ∛((x+1)²M³) − ∛(x²M³) ≤ 2M/3 puts the next root below
  s + 1 + 2M/3, so its floor is at most s + M for every M ≥ 1. Taking one
  more x reuses the converged s.
- The window test: the budget starts at nM + n, so a multiset in the window
  leaves a residual 0 ≤ b < n. There `n<=b<=s` fails, and `f` keeps taking x
  on an ever more negative budget until Python raises `RecursionError`.
  `except:M*=2` catches it and runs the same n again at twice the scale. A
  pass that finishes had no multiset in the window, and `print` writes the
  count minus the empty multiset.

**Why it is exact, and why it does not stall**

- A printed term rests only on a pass that met no multiset in the window,
  computed in integers, so it is never wrong.
- A multiset whose true sum is exactly n has only cube parts, so its C is
  exactly nM, outside the window. That is Besicovitch's theorem
  (A. S. Besicovitch, *On the linear independence of fractional powers of
  integers*, J. London Math. Soc. 15 (1940), 3–6): cube roots of distinct
  cube-free integers are linearly independent over ℚ. A non-cube x has
  x^(2/3) = r·m^(1/3) with r rational and m > 1 cube-free, and the
  coefficients only add up, so any sum with a non-cube part is irrational.
- Every other multiset misses n by some δ > 0. One with T > n has
  C ≥ T·M > nM + n once M > n/δ; one with T < n has C < T·M + k ≤ nM once
  M ≥ k/δ. Only multisets with T ≤ 2n can ever be in the window, finitely
  many, so some M clears them all.
- M doubles only after a failed pass and never goes down. It is 2²³ by
  n = 22 and 2²⁴ by n = 29, after 24 failed passes in all.

**Notes**

- The time follows a(n), which multiplies by about 1.45 per term near
  n = 29. The program prints 27 terms in about 24 s and 29 in a minute. The
  bar is 26 terms in 60 s.
- Newton's steps stay on the stack like the parts, so the deepest call is the
  run of x = 1, 2, … from the root with about five frames per x: about 650
  frames at n = 29. The default recursion limit of 1000 is reached near
  n = 38, past the 35 terms of the b-file and hours away. From there on even
  a clean pass raises `RecursionError`, and the program keeps doubling M
  without printing.
- The bare `except` would catch any error, but nothing else can happen: s is
  0 only for x = 1 at M = 1, after Newton's method has stopped, so `v//s`
  never divides by 0.
- Discarded variants: two passes with budgets nM and nM + n compared through
  `a,b=[f(n*M+e,M,M)for e in(0,n)];n+=a==b!=print(a-1)`, with M doubled
  every pass, came to 165 bytes and reached 27 terms in a minute. The
  A000135 program with `f(b-W[i],i)` (a list of floor and ceiling weights,
  two passes) comes to 209 bytes; it is about five times faster and prints
  33 terms in 32 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 157 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000234), CC BY-SA 4.0.
