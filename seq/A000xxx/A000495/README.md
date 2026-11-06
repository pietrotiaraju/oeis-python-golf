# A000495

> Nearest integer to sinh(n).
> — [OEIS A000495](https://oeis.org/A000495)

Offset 0: 0, 1, 4, 10, 27, 74, 202, 548, 1490, 4052, …

### Python 3 — 113 bytes

```python
n=0
while 1:
 N=n;F=d=1
 while -(2*N+F)%(2*F)<2*n**d:d+=2;N=N*d*(d-1)+n**d;F*=d*(d-1)
 print((2*N+F)//(2*F));n+=1
```

**How it works**

- Sum the positive series sinh(n)=Σ_(d positive odd) nᵈ/d!.
  The state N/F is its partial sum through odd degree d, with
  F=d!. Initially N=n, F=d=1 includes the first term.
- To add the next term, increase d by 2, multiply N and F by
  d(d−1), and add nᵈ to N. Both the old sum and new term
  then have the same factorial denominator.
- The last term t=nᵈ/d! bounds the unsummed tail once d≥2n+1:
  subsequent term ratios are less than 1/4, so the tail is
  less than t·(1/4+1/16+…)=t/3<t.
- Stopping cannot happen earlier for positive integer n. For
  d≤2n−1, AM–GM gives d!≤((d+1)/2)ᵈ≤nᵈ, so t≥1.
  The distance to the next rounding boundary is always less
  than 1 and therefore fails the stopping test in this range.

- Nearest-integer rounding is floor(sinh(n)+1/2). For the
  partial value, use (2N+F)/(2F). The numerator
  `-(2*N+F)%(2*F)` is its distance to the next integer
  boundary, scaled by 2F; compare it with `2*n**d`.
  Stop when the gap is at least the tail bound, then print
  `(2*N+F)//(2*F)`.

- At an exact partial-sum boundary the modular gap is zero,
  which conservatively forces another term. At n=0 the tail
  bound is zero and the loop immediately prints 0.

**Notes**

- **Termination.** For n>0, exp(n) is transcendental by
  [Hermite–Lindemann](https://mathworld.wolfram.com/Hermite-LindemannTheorem.html).
  If sinh(n)=s were algebraic, exp(n) would solve
  z²−2sz−1=0 and be algebraic too. Thus sinh(n) is not
  an integer or half-integer; convergence of the series and
  decay of the tail bound eventually resolve every output.
- Exact integer arithmetic with an adaptive number of terms,
  rather than a fixed precision approximation to sinh.
  [A000471](../A000471/) uses the same series with
  integer rounding boundaries.
- The factorial denominator and powers grow during each evaluation,
  which restarts at the next n. The outputs eventually meet Python
  3.11+'s default 4300-digit conversion limit, an interpreter limit.
- The b-file has 251 terms (indices 0 through 250). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 113 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000495), CC BY-SA 4.0.
