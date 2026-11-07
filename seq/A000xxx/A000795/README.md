# A000795

> Salié numbers: expansion of cosh x / cos x = Sum_{n >= 0} a(n)*x^(2n)/(2n)!.
> — [OEIS A000795](https://oeis.org/A000795)

Offset 0: 1, 2, 12, 152, 3472, 126752, 6781632, 500231552, 48656756992, 6034272215552, 929327412759552, 174008703107274752, 38928735228629389312, 10255194381004799025152, 3142142941901073853366272, …

### Python 3 — 70 bytes

```python
r=[s:=1]
while[print(s)]:
 for s in 0,1:r=[s:=s+x for x in[0]+r[::-1]]
```

**How it works**

- cosh x is even and tan x is odd, so the even part of
  (sec x + tan x)·cosh x is sec x·cosh x = cosh x / cos x. The product with
  sec x + tan x is the boustrophedon transform: in the triangle
  T(n,0) = u(n), T(n,k) = T(n,k−1) + T(n−1,n−k) (Millar, Sloane and Young),
  with u = 1, 0, 1, 0, … (the coefficients of cosh x), a(n) is the last
  entry of row 2n.
- Each pass builds two rows. `for s in 0,1:` sets the first entry of the
  odd row to 0 and of the even row to 1; the leading `[0]` in
  `[0]+r[::-1]` keeps that start, and then `s` adds the old row reversed.
  After the pass `s` is the last entry of the even row, the next term.

**Notes**

- Printing only the even values is 1 byte longer
  (`r=[0,t:=1]`, `while[t%2*t>1or print(t)]:` and first element `t%2-t`):
  row 2n+1 ends in Σₖ C(2n+1,2k+1)·T(2k+1), which is odd since the tangent
  numbers T(3), T(5), … are even, while a(n) is even for n ≥ 1 (the secant
  numbers are odd and Σₖ C(2n,2k) = 2²ⁿ⁻¹).
- The values were checked for every printed term against
  a(n) = Σₖ C(2n,2k)·E(2n−2k) (Philippe Deléham), with E =
  [A000111](../A000111/).
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(830); the 830 terms
  before it print in about two seconds.
- The b-file has 101 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000795), CC BY-SA 4.0.
