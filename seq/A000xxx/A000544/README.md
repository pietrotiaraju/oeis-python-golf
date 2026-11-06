# A000544

> One-half of the number of permutations p of [n] having exactly two runs of adjacent entries differing by 1.
> — [OEIS A000544](https://oeis.org/A000544)

Offset 4: 3, 25, 155, 1005, 7488, 64164, 619986, 6646750, 78161249, 999473835, …

### Python 3 — 218 bytes

```python
A=[1,1,0,0];F=[0]*4;n=4
while 1:
 A+=(n+1)*A[-1]-(n-2)*A[-2]+(5-n)*A[-3]+(n-3)*A[-4],
 F+=sum(x*y for x,y in zip(A[::-1],(1,-3,5,-3,3,-1)))+(n==4)+sum(x*y for x,y in zip(F[::-1],(5,-9,5,5,-9,5,-1))),
 print(F[-1]);n+=1
```

**How it works**

- Put H(y)=Σₖ₌₀∞ k!y^k and y=x(1−x)/(1+x), as in the OEIS generating
  function. The factorial recurrence gives y²H′+(y−1)H+1=0.
- Write A(x)=H(y). The chain rule yields, for n≥4,
  Aₙ=(n+1)Aₙ₋₁−(n−2)Aₙ₋₂+(5−n)Aₙ₋₃+(n−3)Aₙ₋₄,
  starting with [1,1,0,0]. These are auxiliary series coefficients.
- Eliminating H′ and H″ in the stated generating function gives
  F(x)=(U(x)A(x)+V(x))/D(x), where
  U=1−3x+5x²−3x³+3x⁴−x⁵,
  V=−1+2x−2x²−2x³+x⁴, and D=(1−x)⁶(1+x).
- F has four initial zero coefficients. At n=4 only V₄=1 still
  contributes. The second update extracts the numerator coefficient
  and subtracts the nonconstant part of D·F, whose coefficients are
  [−5,9,−5,−5,9,−5,1]. Printing starts at the required offset 4.

**Notes**

- Both recurrences follow algebraically from the OEIS generating
  function and use integer additions and multiplications only.
- This keeps the full auxiliary history for compact indexing. Large
  outputs eventually meet Python's conversion limit.
- The reference file contains 447 terms from the OEIS b-file; the verification
  bar is 447 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 218 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000544), CC BY-SA 4.0.
