# A000943

> Number of combinatorial types of simplicial n-dimensional polytopes with n+3 nodes.
> — [OEIS A000943](https://oeis.org/A000943)

Offset 1: 1, 2, 5, 8, 18, 29, 57, 96, 183, 318, 604, 1080, 2047, 3762, 7145, 13354, 25471, 48164, 92193, 175780, …

### Python 3 — 104 bytes

```python
import math
m=5
while[print(-m//2+2**(m-3>>1)+sum(2**math.gcd(j,m)for j in range(0,m,m&-m))//4//m)]:m+=1
```

**How it works**

- Perles' formula (Grünbaum, *Convex Polytopes*, §6.3, via Gale diagrams):
  there are 2^⌊d/2⌋ − ⌊(d+4)/2⌋ + (1/(4(d+3))) Σ φ(h) 2^{(d+3)/h}
  simplicial d-polytopes with d+3 vertices, the sum over the odd divisors
  h of d+3.
- The terms are one dimension off the title: a(1) = 1 is the pentagon
  (d = 2, five vertices) and a(2) = 2 the two simplicial 3-polytopes with
  six vertices, so a(n) is Perles' count for d = n+1 (the OEIS Maple
  program does the same). The program follows the data.
- With m = d+3 = n+4 the count is 2^⌊(m−3)/2⌋ − ⌊(m+1)/2⌋ + Σ/(4m). The
  rotation by j of ℤₘ has order m/gcd(j, m), and φ(h) rotations have order
  h; the order is odd exactly when j is a multiple of 2ᵉ ∥ m, which is
  `m&-m`. So Σ = Σ 2^gcd(j,m) over `range(0,m,m&-m)`, 4 B under
  `m//(g:=gcd(j,m))%2<<g` over all j.
- −⌊(m+1)/2⌋ = ⌊−m/2⌋, written first as `-m//2` so it parses as (−m)//2.

**Notes**

- Exact integer arithmetic; correctness rests on Perles' theorem.
- Thousands of terms per second.
- The b-file is synthesized from the 34 terms of the entry; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 104 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000943), CC BY-SA 4.0.
