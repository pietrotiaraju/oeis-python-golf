# A000488

> Generalized tangent numbers d_(n,3).
> — [OEIS A000488](https://oeis.org/A000488)

Offset 1: 16, 361, 3362, 16384, 55744, 152166, 355688, 739328, 1415232, 2529614, …

### Python 3 — 129 bytes

```python
D=[a:=0]
while 1:a+=1;D+=sum((u:=abs(y*y%(4*a)-2*a)-a)*(5*a*a-u*u)**2-D[a//y]*(y%2>a%y)for y in range(2,2*a+2)),;print(D[a]>>1%a)
```

**How it works**

- Let L_n=Σ_(k positive odd) (n|k)/k⁶, with (n|k) the Jacobi
  symbol, and δ(n)=5!·(2n/π)⁶·L_n/√n. This is the
  Dirichlet-series normalization of the generalized tangent number.
  For n>1 it is the desired a(n), but
  δ(1)=8 while the tangent-number convention requires a(1)=16.
  As in [A000176](../A000176/), keep this normalization distinction
  inside the divisor calculation and fix it only when printing.
- The odd-frequency Fourier identity
  Σ_(k positive odd) cos(πkx)/k⁶=−π⁶E_5(x)/480 on [0,1]
  is [DLMF 24.8.5](https://dlmf.nist.gov/24.8.E5).
  Combining it with the quadratic Gauss-sum calculation of A000176
  replaces the infinite character sum by a finite polynomial sum.
- For each residue y mod 2n, put
  u=|y² mod 4n−2n|−n, so −n≤u≤n. Folding the Fourier
  argument into [0,1] gives x=(n−u)/(2n), and
  **−32n⁵E_5(x)=u(5n²−u²)²**. This is the integer polynomial
  in the comprehension; π and the square roots have canceled.
- The Gauss sum also includes odd frequencies sharing factors with n.
  If g_n(u)=u(5n²−u²)² and U(n)=½Σ_y g_n(u), the resulting
  identity is U(n)=Σ_(e odd, e divides n) δ(n/e).
  Subtract the contributions for e>1 to isolate δ(n).
- D stores 2δ(n), beginning with D[0]=0. Thus the new entry is
  Σ_y g_n(u)−Σ_(e>1 odd, e divides n) D[n/e], with no
  division inside either sum. The variable a in the program is n.
- `range(2,2*a+2)` supplies exactly 2n consecutive residues,
  starting beyond the troublesome y=0 and y=1. The test
  `y%2>a%y` is true exactly for odd divisors y of n. For y>n,
  `D[a//y]` is D[0]=0, so the extra residues are harmless.
- `%` binds before `>>`, so `D[a]>>1%a` means D[n] shifted
  by 1%n bits. It halves the stored value for n>1, but leaves
  D[1]=16 intact, giving the exceptional first tangent number.

**Notes**

- At n=1 the two residues give polynomial values 16 and 0,
  hence D[1]=16. At n=2 their sum is 722 and there are no
  proper odd-divisor contributions, so the output is 722/2=361.
- The divisor correction must use δ(1)=8, not the doubled first
  output a(1)=16. Keeping D[1]=2δ(1) makes the recurrence and
  printing conventions agree without another special-case state.
- Exact integer residues, polynomial evaluations and divisor inversion,
  with no numerical Fourier truncation. Each term uses 2n iterations,
  so N outputs require O(N²) summands and a list of N+1 integers.
- [A000176](../A000176/) uses the cubic polynomial
  u(3n²−u²) for the fourth-power Dirichlet series; this page
  uses the fifth-degree polynomial for the sixth-power series.
- The b-file has 1000 terms (indices 1 through 1000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 129 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000488), CC BY-SA 4.0.
