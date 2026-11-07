# A000927

> "First factor" (or relative class number) h- for cyclotomic field Q( exp(2 Pi / prime(n)) ).
> — [OEIS A000927](https://oeis.org/A000927)

Offset 1: 1, 1, 1, 1, 1, 1, 1, 1, 3, 8, 9, 37, 121, 211, 695, 4889, 41241, 76301, 853513, 3882809, …

### Python 3 — 235 bytes

```python
P=p=1
while 1:
 P*=p*p;p+=1
 if P%p:
  r=range(1,p//2+1);M=[[i*pow(j,-1,p)//p for j in r]for i in[p,*r[1:]]];q=1
  while M:(a,*R),*M=sorted(M,key=lambda r:r[0]==0);M=[[(x*a-y*b)//q for x,y in zip(s,R)]for b,*s in M];q=a
  print(abs(q))
```

**How it works**

- Let p = prime(n), g = (p−1)/2 and R(x) the least positive residue mod p.
  Carlitz and Olson (Proc. AMS 6 (1955), 265–269) proved that Maillet's
  determinant det[R(i·j⁻¹)] over 1 ≤ i, j ≤ g is ±p^(g−1)·h⁻.
- Subtracting i times row 1 from row i (i ≥ 2) turns R(i·k) − i·k into
  −p·⌊ik/p⌋, where k = R(j⁻¹) is the entry of row 1. Taking the factor p
  out of those g−1 rows leaves h⁻ = |det N|, where row 1 of N is k itself
  and row i is ⌊ik/p⌋. Since k = ⌊pk/p⌋, every row has the same form:
  N = [⌊i·k/p⌋] with i in (p, 2, 3, …, g), which is `[p,*r[1:]]`, and
  k = `pow(j,-1,p)`. No division by a power of p is left.
- For p = 2 and 3 the matrix is the 1×1 matrix [1], giving h⁻ = 1 (a(1) = 1
  by convention for p = 2).
- The determinant is fraction-free (Bareiss) elimination: each step takes
  a row `(a,*R)` with a nonzero first entry as pivot, replaces every other
  row `(b,*s)` by (a·s − b·R)/q, where q is the previous pivot (the division
  is exact: the new entries are minors of the original matrix), and keeps
  `q=a`. After the last step q is ± the determinant.
- `sorted(M,key=lambda r:r[0]==0)` moves rows with a zero first entry to
  the end, so the pivot is nonzero: one always exists because h⁻ ≥ 1, so
  every Schur complement is nonsingular. Row order only changes the sign,
  and `abs` drops it.
- p runs over the primes by Wilson's theorem: `P` is ((p−1)!)², and
  P mod p is 1 for primes and 0 otherwise.

**Notes**

- Exact integer arithmetic; correctness rests on the Carlitz–Olson
  theorem. The matrix has (p−1)/2 rows, so a term costs about p³/12
  big-integer products: about 95 terms in 60 s.
- The b-file has 100 terms; the bar is 75 terms in 60 s.
- A formula of Max Alekseyev in the OEIS entry, the determinant of
  [⌊ij/p⌋ − ⌊(i−1)j/p⌋] over 3 ≤ i, j ≤ g, matches the data but is not
  used here: no proof of it was found.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 235 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000927), CC BY-SA 4.0.
