# A000521

> Coefficients of modular function j as power series in q = e^(2 Pi i t). Another name is the elliptic modular invariant J(tau).
> — [OEIS A000521](https://oeis.org/A000521)

Offset -1: 1, 744, 196884, 21493760, 864299970, 20245856256, 333202640600, 4252023300096, 44656994071935, 401490886656000, …

### Python 3 — 156 bytes

```python
from math import*
A=[1];n=0
while[print(A[-1])]:
 n+=1;A+=sum(sum((504*d**5-240*(n-k-1)*d**3)for d in range(1,k+1)if k%d<1)*A[n-k]for k in range(1,n+1))//n,
```

**How it works**

- The OEIS coefficient identity is
  (m+1)a(m)=Σₖ₌₁ᵐ⁺¹(504σ₅(k)−240(m−k)σ₃(k))a(m−k), with a(−1)=1.
  It follows from the differential identities for the Eisenstein series
  in j=E₄³/Δ, where E₄=1+240Σσ₃(k)q^k and Δ=q∏(1−q^k)²⁴.
- `A[n]` is a(n−1), so the next coefficient divides by n and uses
  (n−k−1) in the σ₃ factor. The inner sum evaluates both divisor sums
  together, with an exact remainder test.
- The first printed value is the q^−1 coefficient 1. The next is
  504+240=744, including the normalization of the constant term.

**Notes**

- All arithmetic is integral; division by n is exact by the modular
  form identity. This uses no floating point evaluation of q or j.
- The compact divisor scan is expensive at high degree. The bar is the
  first 150 coefficients, with the complete reference file retained.
- The reference file contains 10002 terms from the OEIS b-file; the verification
  bar is 150 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 156 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000521), CC BY-SA 4.0.
