# A000658

> Strehl's sequence "C_n^(3)".
> — [OEIS A000658](https://oeis.org/A000658)

Offset 0: 1, 4, 68, 1732, 51076, 1657904, 57793316, 2117525792, 80483121028, 3147565679824, 125937573689968, …

### Python 3 — 105 bytes

```python
from math import*
n=0
while[print(sum((comb(n,k)*comb(2*k,k))**2*comb(2*k,n-k)for k in range(n+1)))]:n+=1
```

**How it works**

- The OEIS formula a(n) = Σₖ C(n,k)²·C(2k,k)²·C(2k,n−k), k = 0..n, summed
  directly. `comb` returns 0 when n−k > 2k, so the terms with k < n/3
  vanish by themselves.
- C(n,k)²·C(2k,k)² is written as one square, 1 byte under two `**2`.

**Notes**

- A search over sums of products of up to five binomials of the shapes
  C(n,k), C(n+k,k), C(2k,k), C(2k,n), C(2k,n−k), C(3k,n), C(2n,k), … found
  no other formula matching the first terms, so the sum stays as it is.
- Exact integer arithmetic, so the program is right for every n.
- About n²/2 binomials of up to 2n bits for the first n terms: the
  596-term b-file prints in about 12 s, about 1000 terms in 60 s.
  The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 105 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000658), CC BY-SA 4.0.
