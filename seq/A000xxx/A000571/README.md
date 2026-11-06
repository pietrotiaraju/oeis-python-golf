# A000571

> Number of different score sequences that are possible in an n-team round-robin tournament.
> — [OEIS A000571](https://oeis.org/A000571)

Offset 0: 1, 1, 1, 2, 4, 9, 22, 59, 167, 490, …

### Python 3 — 220 bytes

```python
from math import*
A=[1];B=[0];n=0
while[print(A[-1])]:
 n+=1;B+=sum((-1)**(n+d)*sum(gcd(j,n//d)==1 for j in range(1,n//d+1))*comb(2*d,d)for d in range(1,n+1)if n%d<1)//(2*n),
 A+=sum(B[k]*A[n-k]for k in range(1,n+1))//n,
```

**How it works**

- The logarithmic-derivative sequence in OEIS is
  b(n)=(1/(2n))Σ_d|n (−1)^(n+d)φ(n/d)C(2d,d), A145855.
  The inner coprimality count computes Euler's totient exactly.
- With a(0)=1, comparing coefficients in xA′/A=Σb(n)x^n gives
  a(n)=Σₖ₌₁ⁿ b(k)a(n−k)/n. The two lists retain these coefficients.
- This formula counts tournament score sequences, rather than
  tournaments themselves. In particular it produces 22 at n=6 while
  A000568 counts 56 tournament isomorphism classes.

**Notes**

- Both divisions are exact integer identities. No floating point
  polytope volume or empirical recurrence is used.
- The reference file contains 1676 terms from the OEIS b-file; the verification
  bar is 1000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 220 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000571), CC BY-SA 4.0.
