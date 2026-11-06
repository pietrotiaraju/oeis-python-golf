# A000426

> Coefficients of ménage hit polynomials.
> — [OEIS A000426](https://oeis.org/A000426)

Offset 1: 0, 1, 1, 1, 8, 35, 211, 1459, 11584, 103605, …

### Python 3 — 81 bytes

```python
m=b=c=d=1;a=0
while[print(a)]:m+=1;a,b,c,d=b,c,d,m*(b+c+d)+(m*c+d-b)//2+a+(-1)**m
```

**How it works**

- Put b(n)=a(n) for this sequence. It is the normalized ménage hit
  coefficient related to [A000033](../A000033/) by A000033(n)=n·b(n).
  Taking the coefficient of t² in the circular ménage hit polynomial
  gives, for n≥2,

  b(n)=Σₖ₌₂ⁿ (−1)ᵏ(2n−k−1)!(n−k)!/((2n−2k)!(k−2)!).

- The program instead uses the proved order-four recurrence

  2b(n)=(2n−5)b(n−1)+(3n−9)b(n−2)+(2n−7)b(n−3)
  +2b(n−4)−2(−1)ⁿ, for n≥5.

- At a print, `a,b,c,d` hold b(m), …, b(m+3), initially
  0,1,1,1. After `m+=1`, the new last entry is b(m+3).
  Substituting n=m+3 makes its three linear coefficients
  2m+1, 3m and 2m−1, exactly the grouped expression in the update.
- The term `(m*c+d-b)//2` is exact: the recurrence says that its
  numerator is twice b(m+3) minus twice the other integer terms.
  The tuple assignment keeps all four old values available.

**Notes**

- The recurrence has a telescoping certificate and direct checks
  against the finite sum in
  [A000033/recurrence_check.py](../A000033/recurrence_check.py).
  That page also explains the index correction needed for the
  homogeneous recurrence printed on the OEIS page.
- This is the A000033 program with `print(a)` in place of
  `print(m*a)`: normalization saves 2 bytes. For example b(5)=8,
  whereas A000033(5)=40.
- Exact integers and constant-size recurrence state. The factorial
  growth eventually meets Python 3.11+'s default 4300-digit output
  conversion limit, an interpreter limit rather than a wrong term.
- The b-file has 100 terms (indices 1 through 100). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000426), CC BY-SA 4.0.
