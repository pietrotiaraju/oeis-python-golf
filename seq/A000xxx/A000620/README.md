# A000620

> Number of monosubstituted alkanes C(n-1)H(2n-1)-X with n-1 carbon atoms that are stereoisomers.
> — [OEIS A000620](https://oeis.org/A000620)

Offset 1: 0, 0, 0, 0, 2, 6, 20, 60, 176, 512, …

### Python 3 — 156 bytes

```python
from math import*
Q=R=1,;*C,n=0,
while[print(Q[-1]-R[-1])]:C+=sumprod(Q[::3],r:=Q[::-3]),;Q+=0,0,(sumprod(C,r)+2*Q[n])//3;R+=0,sumprod(R[::2],R[n::-1]);n+=1
```

**How it works**

- T(x) = ΣTₖxᵏ counts steric radicals ([A000625](../A000625/)):
  T = 1 + x(T(x)³ + 2T(x³))/3, the cycle index of the rotations C₃ of
  the three branches. A(x) counts radicals without an asymmetric carbon
  ([A000621](../A000621/)): A = 1 + x·A(x)·A(x²).
- A radical without an asymmetric carbon has a single steric form
  (each carbon has two equal branches, so only one cyclic order), and
  the other radicals contribute one term of T per stereoisomer. So in
  Blair and Henze's notation T = As + An, and
  **a(n) = Tₙ₋₁ − Aₙ₋₁**.
- `Q` stores T with two zeros between terms (Q[3e] = Tₑ), so `Q[n]` is
  [xⁿ]T(x³); `C` caches [xⁿ]T(x)², and `sumprod(C,r)` with the
  reversed list `r` is [xⁿ]T(x)³ (as in A000625).
- `R` stores A with one zero between terms (R[2e] = Aₑ): `R[::2]` is
  A₀,…,Aₙ and `R[n::-1]` lists the coefficients of A(x²) from xⁿ down
  to x⁰, so their dot product is Aₙ₊₁.
- The header prints Tₖ − Aₖ = `Q[-1]-R[-1]` before each step.

**Notes**

- Exact integer arithmetic, O(n) per term; both divisions are exact
  orbit counts.
- The reference file has the 1930 terms of the OEIS b-file; the bar is
  all 1930 in 60 s (the program needs about 15 s here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 156 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000620), CC BY-SA 4.0.
