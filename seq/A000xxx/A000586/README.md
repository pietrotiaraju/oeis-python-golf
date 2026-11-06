# A000586

> Number of partitions of n into distinct primes.
> — [OEIS A000586](https://oeis.org/A000586)

Offset 0: 1, 0, 1, 1, 0, 2, 0, 2, 1, 1, …

### Python 3 — 188 bytes

```python
from math import*
n=1
while 1:
 A=[1]+[0]*(n-1)
 for p in range(2,n):
  if all(p%d for d in range(2,isqrt(p)+1)):
   for j in range(n-1,p-1,-1):A[j]+=A[j-p]
 print(*A[n//2:],sep='\n');n*=2
```

**How it works**

- A truncated coefficient array begins with the empty partition, 1.
  For each prime p<n, multiply its generating polynomial by 1+x^p.
- The descending update `A[j]+=A[j-p]` uses each prime at most once.
  Processing j upwards instead would count repeated primes and give a
  different sequence.
- The truncation length doubles each round. Coefficients below n/2
  were already printed, so only the new half is emitted. At n=1 that
  half contains the initial a(0)=1.
- Trial division through isqrt(p) is an exact primality test; primes
  at least n cannot affect coefficients of degree below n.

**Notes**

- Every coefficient is a finite exact integer count. Doubling avoids
  rebuilding the polynomial separately for every output term.
- `sep` emits one term per line, as required.
- The reference file contains 10001 terms from the OEIS b-file; the verification
  bar is 10001 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 188 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000586), CC BY-SA 4.0.
