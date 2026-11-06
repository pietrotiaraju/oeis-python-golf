# A000598

> Number of rooted ternary trees with n nodes; number of n-carbon alkyl radicals C(n)H(2n+1) ignoring stereoisomers.
> — [OEIS A000598](https://oeis.org/A000598)

Offset 0: 1, 1, 1, 2, 4, 8, 17, 39, 89, 211, …

### Python 3 — 158 bytes

```python
from math import*
A=1,;*C,n=0,
while 1:
 C+=sumprod(A,A[::-1]),
 A+=(sumprod(C,A[::-1])+3*sumprod(A[:n//2+1],A[::-2])+2*(n%3<1)*A[n//3])//6,
 print(A[n]);n+=1
```

**How it works**

- Let A(x) count rooted alkyl radicals, including A₀=1 for the empty
  branch. Pólya's S₃ cycle index gives
  A(x)=1+x(A(x)³+3A(x)A(x²)+2A(x³))/6.
- `C[n]` is the coefficient of A(x)². The next update uses this cached
  square to obtain Aₙ₊₁ with two one-dimensional convolutions.
- Write H₂(A)=(A(x)²+A(x²))/2 and H₃(A)=(A(x)³+3A(x)A(x²)+2A(x³))/6.
  Two nonempty unordered branches have series H₂(A)−A; three have
  H₃(A)−H₂(A). Adding the central carbon contributes one factor x.
- A000598 prints Aₙ. A000599 and A000600 first print their zero
  constant term, then print respectively `[x^n](H₂(A)−A)` and
  Aₙ₊₁−[x^n]H₂(A). Removing the empty branch enforces secondary
  and tertiary alcohols rather than primary ones.

- The coefficient lists in the first two convolutions have length
  n+1. `sumprod(A,A[::-1])` gives [x^n]A(x)² and
  `sumprod(C,A[::-1])` gives [x^n]A(x)³ after the square
  coefficient is appended.
- For A(x)A(x²), pair A₀,…,A_⌊n/2⌋ with
  Aₙ,Aₙ₋₂,… . Before appending Aₙ₊₁, these are exactly
  `A[:n//2+1]` and `A[::-2]`, whose lengths agree.
  All inputs are integers, so all three dot products are exact.
- A is a tuple of the radical coefficients; the starred assignment
  initializes an empty square-coefficient list C and counter n=0.

**Notes**

- Cycle-index divisions are exact orbit counts. There is no
  stereochemical distinction, matching the OEIS definitions.
- Caching the square reduces the per-term work to O(n) arithmetic
  operations. Large integer output eventually meets Python's limit.
- The reference file contains 1001 terms from the OEIS b-file; the verification
  bar is 1001 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 189 | first entry |
| 2026-11-06 | Python 3 | 158 | use exact sumprod convolutions and compact coefficient initialization |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000598), CC BY-SA 4.0.
