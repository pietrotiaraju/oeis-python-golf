# A000439

> Powers of rooted tree enumerator.
> — [OEIS A000439](https://oeis.org/A000439)

Offset 1: 9, 30, 69, 133, 230, 369, 560, 814, 1143, 1560, …

### Python 3 — 51 bytes

```python
n=1
while 1:print(n*(n*(n*(n+18)+83)+114)//24);n+=1
```

**How it works**

- The polynomial given by the OEIS is
  a(n)=(n⁴+18n³+83n²+114n)/24 for n≥1.
  Horner's rule factors its numerator as
  n·(n·(n·(n+18)+83)+114), the expression in the program.
- This form needs no explicit powers or separate stored coefficients.
  `n=1` gives (1+18+83+114)/24=9; the next substitution
  gives a(2)=30.
- Exact divisibility is also visible in the binomial-basis identity

  **a(n)=9C(n,1)+12C(n,2)+6C(n,3)+C(n,4).**

  Expanding these four binomial polynomials gives the same quartic,
  so its quotient is integral for every positive integer n.

**Notes**

- Exact integer arithmetic from the stated polynomial, with no
  approximation to a rooted-tree generating function at runtime.
- A quartic has constant fourth differences and zero fifth
  differences. This explains the alternative recurrence signature
  (5,−10,10,−5,1) on the OEIS page, but that approach needs five
  preceding values; the direct expression retains only the index.
- Starting at n=0 would print an extra zero. The offset is 1,
  so the loop begins with the first positive index instead.
- The b-file has 43 terms (indices 1 through 43). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 51 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000439), CC BY-SA 4.0.
