# A000623

> Number of monosubstituted alkanes C(n)H(2n+1)-X of the form shown in the Comments lines that are stereoisomers.
> — [OEIS A000623](https://oeis.org/A000623)

Offset 1: 0, 0, 0, 0, 0, 0, 6, 18, 66, 208, …

### Python 3 — 186 bytes

```python
from math import*
Q=R=1,;*C,n=0,
while 1:C+=sumprod(Q[::3],r:=Q[::-3]),;Q+=0,0,(sumprod(C,r)+2*Q[n])//3;R+=0,sumprod(R[::2],R[n::-1]);print(Q[-1]+Q[-4]-C[n]-R[-1]+R[-3]+R[n]-2*0**n);n+=1
```

**How it works**

- The form in the entry is the tertiary one: the carbon that holds X
  carries three nonempty alkyl groups. T(x) counts steric radicals
  ([A000625](../A000625/), T = 1 + x(T(x)³ + 2T(x³))/3) and A(x) counts
  radicals without an asymmetric carbon ([A000621](../A000621/),
  A = 1 + x·A(x)·A(x²)).
- All steric tertiary radicals: three nonempty branches up to rotation,
  [xⁿ⁻¹]((T − 1)³ + 2(T(x³) − 1))/3. Expanding and using
  T − 1 = x(T³ + 2T(x³))/3, this is Tₖ₊₁ − Cₖ + Tₖ − [k = 0] with
  k = n − 1 and Cₖ = [xᵏ]T².
- The ones without an asymmetric carbon ([A000624](../A000624/)): two
  equal non-stereoisomeric branches and a third one,
  [xᵏ](A(x²) − 1)(A − 1) = Aₖ₊₁ − Aₖ − [2 | k]Aₖ/₂ + [k = 0]. Each has
  one steric form, so the difference counts the stereoisomers:
  **a(n) = Tₖ₊₁ + Tₖ − Cₖ − Aₖ₊₁ + Aₖ + [2 | k]Aₖ/₂ − 2[k = 0]**.
- The lists are those of [A000620](../A000620/): `Q` holds T with two
  zeros between terms, `C` the square of T, `R` holds A with one zero
  between terms. After both appends, `Q[-1]`, `Q[-4]` are Tₖ₊₁, Tₖ,
  `R[-1]`, `R[-3]` are Aₖ₊₁, Aₖ, and `R[n]` is [xⁿ]A(x²) without a
  parity test; `2*0**n` is the k = 0 correction.

**Notes**

- Exact integer arithmetic, O(n) per term.
- The reference file has the 1930 terms of the OEIS b-file; the bar is
  all 1930 in 60 s (the program needs about 12 s here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 186 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000623), CC BY-SA 4.0.
