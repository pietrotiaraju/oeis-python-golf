# A000622

> Number of monosubstituted alkanes C(n)H(2n+1)-X of the form shown in the Comments lines that are stereoisomers.
> — [OEIS A000622](https://oeis.org/A000622)

Offset 1: 0, 0, 0, 2, 4, 14, 34, 98, 270, 768, …

### Python 3 — 170 bytes

```python
from math import*
Q=R=1,;*C,n=0,
while 1:C+=sumprod(Q[::3],r:=Q[::-3]),;print(C[n]-2*Q[-1]-R[n]+2*0**n);Q+=0,0,(sumprod(C,r)+2*Q[n])//3;R+=0,sumprod(R[::2],R[n::-1]);n+=1
```

**How it works**

- The form in the entry is the secondary one, R–CH(X)–R′ with R and R′
  nonempty alkyl groups. T(x) counts steric radicals
  ([A000625](../A000625/), T = 1 + x(T(x)³ + 2T(x³))/3) and A(x) counts
  radicals without an asymmetric carbon ([A000621](../A000621/),
  A = 1 + x·A(x)·A(x²)).
- Seen from X, the substituents H, R, R′ of the central carbon have a
  cyclic order, and starting the reading at H makes it an ordered pair
  (R, R′): all steric secondary radicals with n carbons are
  [xⁿ⁻¹](T − 1)². The ones without an asymmetric carbon need R = R′
  with R itself non-stereoisomeric: [xⁿ⁻¹](A(x²) − 1). Each of those
  has one steric form, so
  **a(n) = [xⁿ⁻¹]((T − 1)² − A(x²) + 1)**.
- With k = n − 1 this is Cₖ − 2Tₖ − [2 | k]Aₖ/₂ + 2[k = 0], where
  Cₖ = [xᵏ]T². The lists are those of [A000620](../A000620/): `Q` holds
  T with two zeros between terms, `C` the square, and `R` holds A with
  one zero between terms, so `R[n]` is [xⁿ]A(x²) without a parity
  test. `2*0**n` adds the 2 only at k = 0.
- The term is printed after `C` gets Cₖ and before `Q` and `R` grow, so
  `Q[-1]` is still Tₖ.

**Notes**

- Exact integer arithmetic, O(n) per term.
- The reference file has the 1930 terms of the OEIS b-file; the bar is
  all 1930 in 60 s (the program needs about 15 s here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 170 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000622), CC BY-SA 4.0.
