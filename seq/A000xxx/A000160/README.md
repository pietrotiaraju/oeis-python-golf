# A000160

> Number of partitions into non-integral powers.
> — [OEIS A000160](https://oeis.org/A000160)

Offset 4: 1, 2, 8, 21, 48, 99, 186, 330, 556, 895, 1397, 2107, 3097, 4459, 6264, 8644, …

### Python 3 — 188 bytes

```python
n=4
f=lambda k,t,i=2:k<1or t>=V[i]and f(k-1,t-V[i],i)+f(k,t,i+1)
while V:=[M:=n**200]:
 for x in range(n*n):
  r=x*M;N=r*r*M
  while r**3>N:r=(2*r+N//r//r)//3
  V+=r,
 print(f(4,n*M));n+=1
```

**How it works**

- As the OEIS comment puts it, a(n) counts the quadruples
  1 ≤ x₁ ≤ x₂ ≤ x₃ ≤ x₄ of integers with x₁^(2/3) + x₂^(2/3) + x₃^(2/3) +
  x₄^(2/3) ≤ n. This is the four-part version of
  [A000148](../A000148/), but the trick used there (cube both sides of
  u + v ≤ n) does not stretch to four cube roots, so the program works in
  fixed point instead.
- With M = n²⁰⁰, the list holds V(x) = ⌊x^(2/3)·M⌋ = ⌊∛(x²M³)⌋, computed
  exactly by integer Newton from r = xM, which is above the root. A step
  ⌊(2r + ⌊N/r²⌋)/3⌋ equals ⌊(2r + N/r²)/3⌋, so by AM–GM it never drops below
  ⌊∛N⌋, and it is smaller than r while r³ > N. The loop therefore stops at
  ⌊∛N⌋ exactly.
- `V:=[M:=n**200]` sets M and starts the list in one go (a non-empty list
  keeps the `while` going). V[0] = M and V[1] = 0 (x = 0) are never used:
  V[i] is the value for x = i − 1, and the count starts at i = 2.
- f(k,t,i) counts the non-decreasing choices of k entries from V[i], V[i+1],
  … with sum at most t: either take V[i] once more (k − 1 parts left, budget
  t − V[i], same i) or move on to i + 1. V is increasing from i = 2, so the
  first V[i] > t ends the branch; t ≤ nM is below the last entry,
  ⌊(n² − 1)^(2/3)·M⌋, so the index never runs off the list.
- Why the floors give the exact count. Each V(x) is at most x^(2/3)·M, so a
  quadruple with s = Σ xᵢ^(2/3) ≤ n has Σ V ≤ nM and is counted, equality
  cases such as 1, 1, 1, 1 at n = 4 included. Each V(x) is also above
  x^(2/3)·M − 1, so a quadruple with s > n has Σ V > sM − 4, and it is left
  out as soon as (s − n)·M ≥ 4. That always holds:
  - if s ≥ n + 1 it is clear (M ≥ 4);
  - otherwise δ = s − n is a non-zero algebraic integer (each xᵢ^(2/3) is a
    root of t³ − xᵢ²) of degree at most 3⁴ = 81. Its conjugates are
    Σ ωʲⁱ·xᵢ^(2/3) − n with ω a cube root of unity, all of absolute value
    below s + n < 2n + 1. The norm of δ is a non-zero integer, so
    δ ≥ (2n + 1)⁻⁸⁰, and M = n²⁰⁰ ≥ 4(2n + 1)⁸⁰ for every n ≥ 4.
- The entries only need x < n², which covers every part: xᵢ^(2/3) ≤ n − 3
  gives xᵢ ≤ (n − 3)^(3/2) < n².

**Notes**

- The whole b-file (38 terms) prints in about 9 s, so the bar is all 38
  terms in 60 s.
- f stops a branch at V[i] > t rather than at k·V[i] > t. The tighter test
  costs 2 bytes and saves no measurable time.
- The recursion depth is about the largest index reached, roughly n^(3/2),
  so Python's default limit of 1000 stops the program near n = 100, far past
  the 60 s mark.
- Doing the roots in a recursive lambda inside a list comprehension comes to
  190 bytes. `exec` of the Newton loop inside the comprehension is shorter
  but does not work: in Python 3.12 the comprehension cannot read back the
  `r` that `exec` sets.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 188 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000160), CC BY-SA 4.0.
