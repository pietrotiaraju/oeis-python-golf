# A001496

> Number of 4 X 4 matrices with nonnegative integer entries and row and column sums equal to n.
> — [OEIS A001496](https://oeis.org/A001496)

Offset 0: 1, 24, 282, 2008, 10147, 40176, 132724, 381424, 981541, 2309384, …

### Python 3 — 68 bytes

```python
x=2
while[print((x**3-x)*(11*x**6+23*x**4+128*x*x+306)//11340)]:x+=1
```

**Why the formula**

- The 4 × 4 tables with all line sums n are the lattice points of n times
  the Birkhoff polytope B₄, whose vertices (the permutation matrices) are
  integral. By Ehrhart's theorem their number H(n) is a polynomial in n of
  degree dim B₄ = 9 (Stanley, *Enumerative Combinatorics* 1, Section 4.6,
  where H₄ is given explicitly on pp. 233–234; Bell's formula in the entry,
  C(n+3,3) + 20·C(n+4,5) + 152·C(n+5,7) + 352·C(n+6,9), is the same
  polynomial).
- With x = n + 2 it factors as

  **H = x(x² − 1)(11x⁶ + 23x⁴ + 128x² + 306) / 11340.**

  A polynomial of degree 9 is fixed by ten values, and this one matches
  H(0), …, H(11) counted by brute force (row by row over column-sum
  vectors), so it is H for every n. The shape is no accident: Ehrhart
  reciprocity gives H(−1) = H(−2) = H(−3) = 0 and H(−4 − n) = −H(n), so H
  is odd in x = n + 2 and has the roots x = 0, ±1.

**How it works**

- The loop runs over x = n + 2 from 2; `x**3-x` is x(x² − 1) =
  (n + 1)(n + 2)(n + 3). The product is a multiple of 11340 because H(n)
  is an integer, so `//` is exact.

**Notes**

- Exact integer arithmetic; correct for every n by Ehrhart's theorem.
- `from math import*` and Bell's four binomials take 100 bytes; Horner in
  y = x² with a walrus, `x*((y:=x*x)-1)*(((11*y+23)*y+128)*y+306)`, is 2
  bytes longer.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001496), CC BY-SA 4.0.
